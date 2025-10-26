const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

describe('build script', () => {
  test('runs build.js and produces dist/index.html', () => {
    // Run the build script (should be fast & idempotent)
    execSync('node build.js', { stdio: 'inherit' });
    const file = path.resolve(__dirname, '..', 'dist', 'index.html');
    const exists = fs.existsSync(file);
    expect(exists).toBe(true);
  }, 10000);
});
