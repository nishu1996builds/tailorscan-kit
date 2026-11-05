const { chromium } = require('playwright');
const fs = require('fs');
const mark = fs.readFileSync(__dirname + '/mark.svg', 'utf8');
const font = "system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif";
const jobs = [
  ['avatar-800.png', 800, 800, `<div style="width:800px;height:800px">${mark.replace('<svg', '<svg width="800" height="800"')}</div>`],
  ['producthunt-240.png', 240, 240, `<div style="width:240px;height:240px">${mark.replace('<svg', '<svg width="240" height="240"')}</div>`],
  ['wordmark-1200x360.png', 1200, 360, `<div style="width:1200px;height:360px;background:#fff;display:flex;align-items:center;gap:40px;padding:0 80px;box-sizing:border-box;font-family:${font}">${mark.replace('<svg', '<svg width="200" height="200"')}<span style="font-size:120px;font-weight:800;letter-spacing:-.03em;color:#16181d">Tailor<span style="color:#1F6F5C">Scan</span></span></div>`],
  ['cover-1640x624.png', 1640, 624, `<div style="width:1640px;height:624px;background:#0f3d33;color:#fff;display:flex;align-items:center;gap:56px;padding:0 140px;box-sizing:border-box;font-family:${font}">${mark.replace('<svg', '<svg width="240" height="240"')}<div><div style="font-size:110px;font-weight:800;letter-spacing:-.03em">TailorScan</div><div style="font-size:46px;color:#d4ece4;margin-top:10px">Free, private resume vs. job description scanner</div></div></div>`],
];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [name, w, h, html] of jobs) {
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<html><body style="margin:0">${html}</body></html>`);
    await p.screenshot({ path: __dirname + '/' + name, omitBackground: name.includes('avatar') || name.includes('producthunt') });
  }
  await b.close(); console.log('rendered', jobs.length);
})();
