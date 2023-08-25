from selenium import webdriver
from time import sleep
from tinder import Tinder
from dotenv import dotenv_values

config = {**dotenv_values('.env')}

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://tinder.com/app/recs")

tinder = Tinder(driver)
sleep(5)
tinder.accept_cookies()
sleep(10)
tinder.clicking_login()
sleep(5)
tinder.login_with_facebook(config['email'], config['pass'])
sleep(600)
