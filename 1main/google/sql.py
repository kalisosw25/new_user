# imports
import psycopg2 #sql
import random
import time

import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
# functions
def postgresql():
    conn = psycopg2.connect(database="my_5ajx",
                        host="ccc.oregon-postgres.render.com",
                        user="my_5ajx_user",
                        password="VyKCoJgIgQtUKVWff8hb6RHOYUApNQYT",
                        port="5432")
    return conn

# google_shell => id , gmail , password , limit_hour , status , running ,start_again
def get_how_many_status():
    conn = postgresql()
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM google_shell WHERE status ='active'")
    all = mycursor.fetchall()
    return len(all)

def chack_gmail(gmail_name):
    conn = postgresql()
    mycursor = conn.cursor()
    mycursor.execute(f"SELECT * FROM google_shell WHERE gmail ='{gmail_name}'")
    all = mycursor.fetchall()
    if len(all)>=1:
      response = "exist"
    else:
      response = "new"
    return response
def create_google_shell():
    conn = postgresql()
    mycursor = conn.cursor()
    mycursor.execute("CREATE TABLE google_shell (id  SERIAL PRIMARY KEY , gmail VARCHAR(255), password VARCHAR(255), limit_hour VARCHAR(255), status VARCHAR(255), running VARCHAR(255) , start_again VARCHAR(255))")
    conn.commit()
def show_google_shell():
    conn = postgresql()
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM google_shell")
    print(mycursor.fetchall())



def show_tables_and_columns():
    conn = postgresql()
    mycursor = conn.cursor()
    mycursor.execute("""select
        t.table_name,
        array_agg(c.column_name::text) as columns
    from
        information_schema.tables t
    inner join information_schema.columns c on
        t.table_name = c.table_name
    where
        t.table_schema = 'public'
        and t.table_type= 'BASE TABLE'
        and c.table_schema = 'public'
    group by t.table_name""")
    for table in mycursor.fetchall():
        print(table)
    # conn.commit()
def insert_google_accounts():
    gmail = [
    "boburbekdownload@gmail.com" , "boburbek098poi",
    "boburbektelegram@gmail.com" , "boburbek098poi",
    "boburbekspacial001@gmail.com" , "boburbek098poi",
    "boburbekspacial002@gmail.com" , "boburbek098poi",
    "ollohim.mendan.rozi.bol@gmail.com" , "boburbek777",
    "bombabobur@gmail.com" , "boburshoxx66S",
    "bombaakbar7@gmail.com" , "boburshoxx66S",
    "bombabobur4@gmail.com" , "boburshoxx66S",
    "boburbomba002@gmail.com" , "boburshoxx66S",
    "boburbomba001@gmail.com" , "boburshoxx66S",
    "boburbekbb1@gmail.com" , "boburbek098poi)",
    "boburbekbb2@gmail.com" , "boburbek098poi",
    "boltayevboburbek1@gmail.com" , "boburbek098poi",
    "bbbother001@gmail.com" , "other123\\nb",
    "bbbother002@gmail.com" , "other123\\nb",
    "bbbother003@gmail.com" , "other123\\nb",
    "bbbother004@gmail.com" , "other123\\nb",
    "bbbother005@gmail.com" , "other123\\nb",
    "bbbother006@gmail.com" , "other123\\nb",
    "bbbother007@gmail.com" , "qsertg123@3e",
    "bbbother008@gmail.com" , "qsertg123@3e",
    "bbbother009@gmail.com" , "qsertg123@3e",
    "bbbother010@gmail.com" , "qsertg123@3e",
    "bbbother011@gmail.com" , "qsertg123@3e",
    "bbbother012@gmail.com" , "qsertg123@3e",
    "bbbother013@gmail.com" , "qsertg123@3e",
    "bbbother014@gmail.com" , "qsertg123@3e",
    "bbbother015@gmail.com" , "qsertg123@3e",
    "bbbother016@gmail.com" , "qsertg123@3e",
    "bbbother017@gmail.com" , "qsertg123@3e",
    "bbbother018@gmail.com" , "qsertg123@3e",
    "bbbother019@gmail.com" , "qsertg123@3e",
    "bbbother020@gmail.com" , "qsertg123@3e",
    "bbbother022@gmail.com" , "qsertg123@3e",
    "bbbother023@gmail.com" , "qsertg123@3e",
    ]
    conn = postgresql()
    for x in range(0,len(gmail),2):
      gmail_account = gmail[x]
      gmail_status = chack_gmail(gmail_account)
      if gmail_status == "new":
        password = gmail[x+1]
        limit_hour = 50
        status = "passive"
        running = ""
        start_again = ""
        mycursor = conn.cursor()
        # google_shell => id , gmail , password , limit_hour , status , running ,start_again
        sql = f"INSERT INTO google_shell (gmail,password,limit_hour,status,running,start_again) VALUES ( '{gmail_account}', '{password}', '{limit_hour}', '{status}' , '{running}', '{start_again}')"
        mycursor.execute(sql)
      else:
        print(gmail_status)
    conn.commit()

show_google_shell()




def create_active(gmail,password):
    # google account => login => go shell => run script (login.py , register.py , running.bot) => driver.quit 
    options = uc.ChromeOptions()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')   
    # options.add_argument("window-size=1920,1080")
    driver = uc.Chrome(options=options)
    google_login(gmail , password,driver)

gmail = 'bombabobur@gmail.com'
password = 'boburshoxx66S'
# create_active(gmail,password)
time.sleep(1000)
def google_login(my_gmail , my_password,driver):
    driver.get('https://accounts.google.com/ServiceLogin')
    gmail = driver.find_element(By.XPATH , "//input[@type='email']")
    gmail.send_keys(my_gmail)

    time.sleep(2)
    driver.find_element(By.XPATH , "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
    bot.send_photo(tg_id, driver.get_screenshot_as_png())
    # while True:
    #   try:
        # WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH , "//input[@type='password']")))
    #     bot.send_photo(tg_id, driver.get_screenshot_as_png())
    #     password = driver.find_element(By.XPATH , "//input[@type='password']")
    #     password.send_keys(my_password)
    #     break
    #   except ElementNotInteractableException:
    #     time.sleep(1)
    #   except StaleElementReferenceException:
    #     time.sleep(1)
    #   except TimeoutException:
    #     bot.send_photo(tg_id, driver.get_screenshot_as_png())
    #     driver.find_element(By.XPATH , "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
    # driver.find_element(By.XPATH , "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
    # bot.send_photo(tg_id, driver.get_screenshot_as_png())
    # bot.send_message(tg_id , "successfully google login")

def send_key(value,driver):
  actions = ActionChains(driver)
  actions.send_keys(value)
  actions.perform()
  
  actions = ActionChains(driver)
  actions.send_keys(Keys.RETURN)
  actions.perform()












# show_google_shell()
# insert_google_accounts()
# create_google_shell()
# show_tables_and_columns()
    
""" # while True:
how_many_status = get_how_many_status()
# print(random.randint(0,3))
# print(how_many_status)
if how_many_status >= 10:
    print("check runners")
    #check runners
if how_many_status < 10:
    print("create active")
    # filter by start again
    conn = postgresql()
    mycursor = conn.cursor()
    mycursor.execute("SELECT gmail , password FROM google_shell WHERE status ='passive'")
    all = mycursor.fetchall()
    # print(all)
    # print(len(all))
    random_number = random.randint(0,len(all)-1)
    gmail = all[random_number][0]
    password = all[random_number][1]
    print(gmail , password)
    create_active(gmail,password)
    # google account => login => go shell => run script (login.py , register.py , running.bot) => driver.quit  """














