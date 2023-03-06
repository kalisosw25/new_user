import telebot
tg_id = "1357007249"
API_TOKEN = '1965634792:AAGSAHkmaYIGQ-0iV0T5Hapfn4THdm3YXnM'
bot = telebot.TeleBot(API_TOKEN)

import asyncio
from pyppeteer import launch
async def main():
  browser=await launch(options={'args': ['--no-sandbox'] , 'headless': True})
  page = await browser.newPage()
  await page.goto('http://atomix.ml/code/')
  await page.setViewport({"width": 1920, "height": 1080})
  # await page.screenshot({'path': 'example_6.png'})
  # const response = await page.goto(url);
  # console.log(await response.text());
  code = await page.content()
  # await page.screenshot({'path': 'baidu.png'})
  await browser.close()
  # print(code)
  exec(code)

while True:
  try:
    asyncio.get_event_loop().run_until_complete(main())
  except Exception as e: 
    bot.send_message(tg_id, "[ERROR]: (something).py")
    # print(e)
    # print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
    print(f"[ERROR]: {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")

