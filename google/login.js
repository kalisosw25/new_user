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
    await page.goto('https://accounts.google.com/');

    var gmail = await page.$x('//input[@type="email"]');
    // var gmail_r = "mira89c382";
    gmail_r = "boburbekbb2@gmail.com"
    await gmail[0].type(gmail_r);
    console.log(gmail_r);

    var next_button = await page.$x('//div[@data-primary-action-label="Next"]//button');
    // console.log(next_button.length);
    await next_button[0].click();

    await sleep(3000);

    var password = await page.$x('//input[@type="password"]');
    // var password_r = "KZuI!j[#N";
    password_r = "boburbek098poi"
    await password[0].type(password_r);
    console.log(password_r);


    var next_button = await page.$x('//div[@data-primary-action-label="Next"]//button');
    await next_button[0].click();

    await sleep(3000);

    await page.screenshot({'path': 'a_1.png'});
    console.log("a_1.png")

    // var button = await page.$x('//button')
    // console.log(button.length)
    // button[1].click();
    // await sleep(3000);
    source = await page.content()

    fs.writeFile('source.html', source, { flag: 'a+' }, err => {});


    await page.screenshot({'path': 'a_2.png'});
    await browser.close() ;
    console.log("finished");
}
doit();
