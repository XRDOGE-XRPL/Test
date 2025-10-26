import asyncio
import json
import os
import pty
import threading
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = ROOT / "public"

app = FastAPI(title="Web-IDE Minimal Backend")

# Serve the static frontend
app.mount("/", StaticFiles(directory=str(PUBLIC_DIR), html=True), name="public")


def safe_path(path: str) -> Path:
    p = (ROOT / path).resolve()
    if ROOT not in p.parents and p != ROOT:
        raise HTTPException(status_code=400, detail="Invalid path")
    return p


@app.get("/api/list")
def list_dir(path: str = ""):
    target = safe_path(path)
    if not target.exists():
        raise HTTPException(status_code=404, detail="Not found")
    if target.is_file():
        return {"type": "file", "name": target.name}
    items = []
    for child in sorted(target.iterdir()):
        items.append({
            "name": child.name,
            "is_dir": child.is_dir(),
        })
    return {"path": str(path), "items": items}


@app.get("/api/read")
def read_file(path: str):
    target = safe_path(path)
    if not target.exists() or not target.is_file():
        raise HTTPException(status_code=404, detail="Not found")
    return FileResponse(str(target))


@app.post("/api/write")
async def write_file(data: dict):
    path = data.get("path")
    content = data.get("content", "")
    if not path:
        raise HTTPException(status_code=400, detail="path required")
    target = safe_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return {"ok": True}


class PtyProcess:
    def __init__(self, cmd=["/bin/bash"]):
        self.cmd = cmd
        self.pid = None
        self.fd = None

    def spawn(self):
        self.pid, self.fd = pty.fork()
        if self.pid == 0:
            # child
            os.execvp(self.cmd[0], self.cmd)

    def read(self, n=1024):
        try:
            return os.read(self.fd, n)
        except OSError:
            return b""

    def write(self, data: bytes):
        try:
            os.write(self.fd, data)
        except OSError:
            pass

    def close(self):
        try:
            os.close(self.fd)
        except Exception:
            pass


@app.websocket("/ws/term")
async def websocket_terminal(websocket: WebSocket):
    await websocket.accept()
    p = PtyProcess()
    p.spawn()

    loop = asyncio.get_event_loop()

    stop_event = threading.Event()

    def reader_thread():
        try:
            while not stop_event.is_set():
                data = p.read(1024)
                if not data:
                    break
                # send to websocket via asyncio
                coro = websocket.send_bytes(data)
                asyncio.run_coroutine_threadsafe(coro, loop)
        except Exception:
            pass

    t = threading.Thread(target=reader_thread, daemon=True)
    t.start()

    try:
        while True:
            msg = await websocket.receive()
            if msg.get("type") == "websocket.receive":
                data = msg.get("bytes") or msg.get("text")
                if isinstance(data, str):
                    p.write(data.encode())
                else:
                    p.write(data)
            elif msg.get("type") == "websocket.disconnect":
                break
    except WebSocketDisconnect:
        pass
    finally:
        stop_event.set()
        p.close()
        try:
            await websocket.close()
        except Exception:
            pass
