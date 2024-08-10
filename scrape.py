import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# initialize the webdriver
os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver-win64\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
#specify the url
url = 'https://in.indeed.com/jobs?q={}&l={}&filter=0&sort=date'

# get the job title and location from the user
job=input('Enter the job title: ')
loc=input('Enter the location: ')

# replace the spaces with '+' in the job title and location
job=job.replace(' ','+')
loc=loc.replace(' ','+')

driver.get(url.format(job,loc))
time.sleep(1+random.random())
button_time = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/div[2]/div/div/div/div[2]/ul/li[1]/div/button')

button_time.click()
time.sleep(1+random.random())
button_24 = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/div[2]/div/div/div/div[2]/ul/li[1]/div/ul/li[1]')
button_24.click()
try:
    time.sleep(1+random.random())
    close=driver.find_element(By.CSS_SELECTOR,'#mosaic-desktopserpjapopup > div.css-g6agtu.eu4oa1w0 > button')
    close.click()
except:
    pass
time.sleep(1+random.random())

while True:
    try:

        jobcard=driver.find_element(By.XPATH,'//*[@id="mosaic-provider-jobcards"]').find_element(By.TAG_NAME,'ul')
        jobs=jobcard.find_elements(By.XPATH, './li')

        for job in jobs:
            try:
                body=job.find_element(By.TAG_NAME,'tbody')
                title=body.find_element(By.TAG_NAME,'a').find_element(By.TAG_NAME,'span').text
                company=body.find_element(By.CSS_SELECTOR, 'span[data-testid="company-name"]').text
                location=body.find_element(By.CSS_SELECTOR,'div[data-testid="text-location"]').text
                salary="Not mentioned"
                job_link=body.find_element(By.TAG_NAME,'a').get_attribute('href')

                try:
                    salary=body.find_element(By.CSS_SELECTOR, 'div.salary-snippet-container').text
                except:
                    pass
                print(title)
                print(company)
                print(location)
                print(salary)
                print(job_link)
                print()
            
            except:
                pass
    except NoSuchElementException:
        break

    time.sleep(2+random.random())
    try:
        next_button=driver.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]')
        next_button.click()
        time.sleep(1+random.random())
    except NoSuchElementException:
        break

while True:
    pass