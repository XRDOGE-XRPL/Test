const fs = require('fs');
const path = require('path');

const src = path.join(__dirname, 'public');
const dest = path.join(__dirname, 'dist');

if (!fs.existsSync(src)) {
  console.error('No public directory to build from.');
  process.exit(1);
}

if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });

const files = fs.readdirSync(src);
files.forEach((f) => {
  const s = path.join(src, f);
  const d = path.join(dest, f);
  fs.copyFileSync(s, d);
});

fs.writeFileSync(path.join(dest, 'build.txt'), `Built at ${new Date().toISOString()}\n`);
console.log('Build successful. Dist created at ./dist');
