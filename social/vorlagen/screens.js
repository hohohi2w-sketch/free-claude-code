const { chromium } = require('playwright');
const path = require('path');
const site = n => 'file://' + path.resolve(process.argv[2], n, 'index.html');
const out = f => path.join(__dirname, 'screens', f);
(async () => {
  const b = await chromium.launch();
  async function open(name, vp, dpr) {
    const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: dpr, colorScheme: 'light', reducedMotion: 'reduce' });
    const p = await ctx.newPage();
    // Freitag, 11:30 Uhr Berliner Zeit: Café ist geöffnet
    await p.clock.install({ time: new Date('2026-11-20T10:30:00Z') });
    await p.goto(site(name));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(1500);
    return { p, ctx };
  }
  for (const n of ['feinschliff', 'mahlgrad', 'halbschatten']) {
    let { p, ctx } = await open(n, { width: 1280, height: 800 }, 1.5);
    await p.screenshot({ path: out(`${n}-desktop.png`) });
    if (n === 'feinschliff') await p.locator('.studio').screenshot({ path: out('feinschliff-studio.png') });
    if (n === 'mahlgrad') {
      await p.locator('.board').screenshot({ path: out('mahlgrad-board.png') });
      await p.locator('#status-hero').screenshot({ path: out('mahlgrad-status.png') });
      console.log('status:', await p.locator('#status-hero').textContent());
    }
    await ctx.close();
    ({ p, ctx } = await open(n, { width: 390, height: 844 }, 2));
    await p.screenshot({ path: out(`${n}-mobile.png`) });
    await ctx.close();
  }
  await b.close();
})();
