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
gmail_r = "mira89c382"
gmail.send_keys(gmail_r)
print(gmail_r)

# driver.save_screenshot("g1.png")

next_button = driver.find_element(By.XPATH , '//div[@data-primary-action-label="Next"]//button')
next_button.click()
time.sleep(3)
# driver.save_screenshot("g2.png")

password = driver.find_element(By.XPATH , '//input[@type="password"]')
password_r = "KZuI!j[#N"
password.send_keys(password_r)
print(password_r)
next_button = driver.find_element(By.XPATH , '//div[@data-primary-action-label="Next"]//button')
next_button.click()

time.sleep(3)
driver.save_screenshot("final.png")
# check loginning
welcome = driver.find_element(By.XPATH , '//*[contains(text(), "Welcome")]')


driver.close() 
print("successfully finished")