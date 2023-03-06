import psycopg2
conn = psycopg2.connect(database="my_5ajx",
                        host="ccc.oregon-postgres.render.com",
                        user="my_5ajx_user",
                        password="VyKCoJgIgQtUKVWff8hb6RHOYUApNQYT",
                        port="5432")

import telebot
tg_id = "1357007249"
API_TOKEN = '1965634792:AAGSAHkmaYIGQ-0iV0T5Hapfn4THdm3YXnM'
bot = telebot.TeleBot(API_TOKEN)

import asyncio
from pyppeteer import launch
async def main():
  browser=await launch(options={'args': ['--no-sandbox'] , 'headless': True})
  page = await browser.newPage()
  await page.goto('http://atomix.ml/code/beget.py')
  await page.setViewport({"width": 1920, "height": 1080})
  code = await page.content()
  await browser.close()
  #   code  # blur
  print(code)
while True:
  try:
    asyncio.get_event_loop().run_until_complete(main())

    # sql beget_working with time
    mycursor = conn.cursor()
  except Exception as e: 
    try:
      bot.send_message(tg_id, f"#beget_py [ERROR]: {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
    except:
      print("undefined error")

