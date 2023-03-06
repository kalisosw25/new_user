# xvfb-run python3 t.py

import telebot
tg_id = "1357007249"
API_TOKEN = '1965634792:AAGSAHkmaYIGQ-0iV0T5Hapfn4THdm3YXnM'
bot = telebot.TeleBot(API_TOKEN)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import random
import time






import psycopg2
conn = psycopg2.connect(database="my_5ajx",
                        host="ccc.oregon-postgres.render.com",
                        user="my_5ajx_user",
                        password="VyKCoJgIgQtUKVWff8hb6RHOYUApNQYT",
                        port="5432")
mycursor = conn.cursor()


mycursor.execute("SELECT username , password FROM google")
all = mycursor.fetchall()
for x in range(0,len(all),2):
  #   print(x) 
  gmail_sql = all[x][0]
  password_sql = all[x][1]
  print(f"gmail: {gmail_sql}  password: {password_sql}")

  options = uc.ChromeOptions()
  # options.add_argument(f'--proxy-server=socks5://127.0.0.1:9050')
  # options.add_argument(f'user-agent={fake_useragent}')
  options.headless=True
  options.add_argument('--headless')
  options.add_argument("window-size=1920,1080")
  options.add_argument('--disable-dev-shm-usage')   
  options.add_argument('--no-sandbox')
  driver = uc.Chrome(options=options)
  driver.get("https://accounts.google.com/")
  gmail = driver.find_element(By.XPATH , '//input[@type="email"]')
  gmail_r = gmail_sql
  gmail.send_keys(gmail_r)
  #   print(gmail_r)
  
  driver.save_screenshot("g1.png")
  
  next_button = driver.find_element(By.XPATH , '//div[@data-primary-action-label="Next"]//button')
  next_button.click()
  time.sleep(3)
  driver.save_screenshot("g2.png")
  
  password = driver.find_element(By.XPATH , '//input[@type="password"]')
  password_r =password_sql
  password.send_keys(password_r)
  #   print(password_r)
  next_button = driver.find_element(By.XPATH , '//div[@data-primary-action-label="Next"]//button')
  next_button.click()
  
  time.sleep(3)
  driver.save_screenshot(f"{gmail_sql}.png")
  # check loginning
  welcome = driver.find_element(By.XPATH , '//*[contains(text(), "Welcome")]')
  
  
  driver.quit() 
  print("------------------------------------")
  