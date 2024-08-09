import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# os.environ['PATH'] += r"C:/SeleniumDrivers"
os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver-win64\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

driver=webdriver.Chrome()
url = 'https://in.indeed.com/jobs?q={}&l={}&filter=0&sort=date'
job='software+developer'
loc='delhi'
driver.get(url.format(job,loc))
time.sleep(1+random.random())
button = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/div[2]/div/div/div/div[2]/ul/li[1]/div/button')

button.click()
time.sleep(1+random.random())
button = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/div[2]/div/div/div/div[2]/ul/li[1]/div/ul/li[1]')
button.click()
try:
    close=driver.find_element(By.CSS_SELECTOR,'#mosaic-desktopserpjapopup > div.css-g6agtu.eu4oa1w0 > button')
    time.sleep(1+random.random())
    close.click()
except:
    pass


while True:
    pass