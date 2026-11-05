// Renders Pinterest pins (1000x1500) for every role and Meta ad creatives (1080x1080).
const { chromium } = require('playwright');
const fs = require('fs');
const roles = JSON.parse(fs.readFileSync('/home/user/tailorscan/data/roles.json', 'utf8'));
const PIN_DIR = '/home/user/tailorscan/src/assets/pins';
const AD_DIR = __dirname + '/ads';
fs.mkdirSync(AD_DIR, { recursive: true });
const esc = s => s.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
const css = `body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}`;
function pin(r) {
  const kws = [...new Set([...r.tools.slice(0, 6), ...r.hard.slice(0, 6)])].slice(0, 10);
  return `<html><head><style>${css}
  .p{width:1000px;height:1500px;background:#0f3d33;color:#fff;padding:80px 70px;box-sizing:border-box;display:flex;flex-direction:column}
  .k{font-size:28px;letter-spacing:.16em;text-transform:uppercase;color:#8fe0c6;font-weight:800}
  h1{font-size:${r.title.length > 26 ? 78 : 92}px;line-height:1.02;margin:22px 0 10px;letter-spacing:-.03em}
  .y{font-size:40px;color:#d4ece4;margin-bottom:44px}
  .card{background:#fff;color:#16181d;border-radius:28px;padding:44px 48px;flex:1}
  .card b{font-size:30px;color:#1f6f5c;text-transform:uppercase;letter-spacing:.08em}
  ul{list-style:none;padding:0;margin:22px 0 0;display:grid;grid-template-columns:1fr 1fr;gap:16px 24px}
  li{font-size:34px;font-weight:700;padding:14px 18px;background:#e3f1ec;border-radius:14px}
  .ex{margin-top:34px;font-size:29px;line-height:1.4;color:#3d4450;border-left:8px solid #1f6f5c;padding-left:20px}
  .f{margin-top:40px;font-size:34px;display:flex;justify-content:space-between;align-items:center}
  .btn{background:#8fe0c6;color:#0f3d33;font-weight:900;padding:18px 28px;border-radius:16px}
  </style></head><body><div class="p"><div class="k">Resume keywords</div><h1>${esc(r.title)}</h1>
  <div class="y">What recruiters and ATS filters search for</div>
  <div class="card"><b>Top keywords to include</b><ul>${kws.map(k => `<li>${esc(k)}</li>`).join('')}</ul><div class="ex"><b style="font-size:24px">Example bullet</b><br>${esc(r.bullets[0])}</div></div>
  <div class="f"><span>Free scanner: TailorScan</span><span class="btn">Check yours free</span></div></div></body></html>`;
}
const ads = [
  { id: 'ad-score', h: 'Your resume scored 47/100 for this job.', s: 'See exactly which keywords are missing. Free, and nothing is uploaded.', badge: '47' },
  { id: 'ad-private', h: 'Free ATS resume scanner.', s: 'No sign-up. No upload. Runs entirely in your browser.', badge: 'FREE' },
  { id: 'ad-silence', h: 'Applying everywhere and hearing nothing?', s: 'Your resume may not use the posting\'s words. Check in 30 seconds.', badge: '30s' },
];
function ad(a) {
  return `<html><head><style>${css}
  .a{width:1080px;height:1080px;background:#0f3d33;color:#fff;padding:90px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between}
  h1{font-size:88px;line-height:1.04;margin:0;letter-spacing:-.03em}
  p{font-size:42px;line-height:1.35;color:#d4ece4;margin:0}
  .row{display:flex;justify-content:space-between;align-items:flex-end}
  .badge{width:230px;height:230px;border-radius:50%;border:18px solid #8fe0c6;display:grid;place-items:center;font-size:${a.badge.length > 2 ? 64 : 92}px;font-weight:900}
  .brand{font-size:40px;font-weight:800}.brand span{color:#8fe0c6}
  </style></head><body><div class="a"><h1>${esc(a.h)}</h1><p>${esc(a.s)}</p>
  <div class="row"><div class="brand"><span>&#9632;</span> TailorScan</div><div class="badge">${a.badge}</div></div></div></body></html>`;
}
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1000, height: 1500 } });
  for (const r of roles) { await p.setContent(pin(r)); await p.screenshot({ path: `${PIN_DIR}/${r.slug}.png` }); }
  await p.setViewportSize({ width: 1080, height: 1080 });
  for (const a of ads) { await p.setContent(ad(a)); await p.screenshot({ path: `${AD_DIR}/${a.id}.png` }); }
  await b.close();
  console.log('pins:', roles.length, 'ads:', ads.length);
})();
