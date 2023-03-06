const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
  }


puppeteer.use(StealthPlugin());
doit = async () => {
    const browser = await puppeteer.launch({args: ['--no-sandbox'], headless: false});
    let page = await browser.newPage();
    await page.setViewport({"width": 1920, "height": 1080}) ;
    await page.goto('https://accounts.google.com/SignUp');

    firstName = await page.$x('//input[@id="firstName"]')
    lastName = await page.$x('//input[@id="lastName"]')
    username = await page.$x('//input[@id="username"]')
    new_password = await page.$x('//input[@name="Passwd"]')
    confirm_password = await page.$x('//input[@name="ConfirmPasswd"]')

    // firstname_r = generate_name()
    // lastname_r = generate_name()
    // username_r = generate_username(9,12)
    // password_r = password_generator(8,11)
    firstname_r = "Madia"
    lastname_r = "Leyla"
    username_r = "celia22cca"
    password_r = "xh9LFiA5S"
    

    await firstName[0].type(firstname_r)
    await sleep(1000);
    await lastName[0].type(lastname_r)
    await sleep(1000);
    await username[0].type(username_r)
    await sleep(1000);
    await new_password[0].type(password_r)
    await sleep(1000);
    await confirm_password[0].type(password_r)
    await sleep(1000);

    // check_error_gmail_name
    await page.screenshot({'path': 'google_reg_1.png'})
    gmail_name_error = await page.$x('//div[@class="LXRPh"]//div[@class="o6cuMc Jj6Lae"]')

    for (let i = 0; i < gmail_name_error.length; i++) {
        text = await (await gmail_name_error[i].getProperty('textContent')).jsonValue()
        if (text.length>10){
            console.log("[ERROR] SignUp : " + text)
        }
      }


    var next_button = await page.$x('//button');
    // console.log(next_button.length);
    await next_button[1].click();

    await sleep(3000);
    await page.screenshot({'path': 'google_reg_last.png'})

    await browser.close()
    console.log("finished")
}
doit();
