const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
  }

const fs = require('fs');
puppeteer.use(StealthPlugin());
doit = async () => {
    const browser = await puppeteer.launch({args: ['--no-sandbox'], headless: false , userDataDir: './myUserDataDir',});
    let page = await browser.newPage();
    await page.setViewport({"width": 1920, "height": 1080}) ;
    await page.goto('https://google.com/');

    await page.screenshot({'path': 'google_check.png'});
    await browser.close() ;
    console.log("finished");
}
doit();
