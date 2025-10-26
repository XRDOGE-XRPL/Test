const http = require('http');
const fs = require('fs');
const path = require('path');

const port = process.env.PORT || 3000;

const serveFile = (filePath, res) => {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.statusCode = 404;
      res.setHeader('Content-Type', 'text/plain; charset=utf-8');
      res.end('Not found');
      return;
    }
    const ext = path.extname(filePath).toLowerCase();
    const map = {
      '.html': 'text/html; charset=utf-8',
      '.js': 'application/javascript',
      '.css': 'text/css',
      '.json': 'application/json',
      '.png': 'image/png',
      '.jpg': 'image/jpeg'
    };
    res.setHeader('Content-Type', map[ext] || 'application/octet-stream');
    res.end(data);
  });
};

const server = http.createServer((req, res) => {
  const safeUrl = decodeURI(req.url.split('?')[0]);
  let filePath = path.join(__dirname, 'public', safeUrl === '/' ? 'index.html' : safeUrl);
  // prevent directory traversal
  if (!filePath.startsWith(path.join(__dirname, 'public'))) {
    res.statusCode = 400;
    res.end('Bad request');
    return;
  }
  serveFile(filePath, res);
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
