// Rendert Profilbild und Beiträge aus posts.html als JPG (Instagram-Größen).
const { chromium } = require('playwright');
const path = require('path');
const NAMES = { avatar: '00-profilbild', p1: '01-hallo', p2: '02-konzept-nagelstudio', p3: '03-konzept-cafe', p4: '04-konzept-fotografin',
  p5: '05-checkliste', p6: '06-detail-cafe', p7: '07-detail-nagelstudio', p8: '08-ablauf', p9: '09-instagram-und-website' };
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'posts.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  for (const [id, name] of Object.entries(NAMES)) {
    await p.locator('#' + id).screenshot({ path: path.join(__dirname, '..', 'bilder', name + '.jpg'), type: 'jpeg', quality: 92 });
  }
  // Übersicht wie im Profilraster (neueste oben links)
  await p.setContent(`<body style="margin:0;background:#fff;display:grid;grid-template-columns:repeat(3,360px);gap:4px;width:1088px">${
    ['09-instagram-und-website','08-ablauf','07-detail-nagelstudio','06-detail-cafe','05-checkliste','04-konzept-fotografin','03-konzept-cafe','02-konzept-nagelstudio','01-hallo']
      .map(n => `<img src="file://${path.join(__dirname, '..', 'bilder', n + '.jpg')}" style="width:360px;height:450px;object-fit:cover;display:block">`).join('')}</body>`);
  await p.waitForTimeout(500);
  await p.screenshot({ path: path.join(__dirname, 'raster.png'), fullPage: true });
  await b.close();
})();
