# xvfb-run python google_login.py
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

from selenium_stealth import stealth

options = uc.ChromeOptions()
# options.add_argument(f'--proxy-server=socks5://127.0.0.1:9050')
# options.add_argument(f'user-agent={fake_useragent}')

# options.headless=False
# options.add_argument('--headless')

options.add_argument("window-size=1920,1080")
options.add_argument('--disable-dev-shm-usage')   
options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-first-run")
options.add_argument("--no-service-autorun")
options.add_argument("--no-default-browser-check")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--profile-directory=Default")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--incognito")
driver = uc.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get("https://accounts.google.com/")
gmail = driver.find_element(By.XPATH , '//input[@type="email"]')
# gmail_r = "mira89c382"
gmail_r = "boburbekbb1"
gmail.send_keys(gmail_r)
print(gmail_r)

# driver.save_screenshot("g1.png")

next_button = driver.find_element(By.XPATH , '//div[@data-primary-action-label="Next"]//button')
next_button.click()
time.sleep(3)
driver.save_screenshot("google_login_pass.png")

password = driver.find_element(By.XPATH , '//input[@type="password"]')
# password_r = "KZuI!j[#N"
password_r = "boburbek098poi"
password.send_keys(password_r)
print(password_r)
next_button = driver.find_element(By.XPATH , '//div[@data-primary-action-label="Next"]//button')
next_button.click()

time.sleep(3)
driver.save_screenshot("final_3.png")
# check loginning
welcome = driver.find_element(By.XPATH , '//*[contains(text(), "Welcome")]')
print(welcome.text)

driver.close() 
print("successfully finished")