import os
import time
import random
import dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_indeed_jobdata(job,loc):
    # load the environment variables
    dotenv.load_dotenv()

    # get the path of the chrome driver
    chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')

    # initialize the webdriver
    os.environ['PATH'] += chrome_driver_path
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--log-level=3") 
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)

    #specify the url
    url = 'https://in.indeed.com/jobs?q={}&l={}&filter=0&sort=date'

    # replace the spaces with '+' in the job title and location
    job=job.replace(' ','+')
    loc=loc.replace(' ','+')

    #format the url
    driver.get(url.format(job,loc))

    time.sleep(1+random.random())

    # click on the time button
    button_time = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="filter-dateposted"]'))
    )
    button_time.click()

    time.sleep(1+random.random())

    # click on the last 24 hours button
    button_24 = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/div[2]/div/div/div/div[2]/ul/li[1]/div/ul/li[1]')
    button_24.click()

    # close the popup if it appears
    try:
        time.sleep(1+random.random())
        close=driver.find_element(By.CSS_SELECTOR,'#mosaic-desktopserpjapopup > div.css-g6agtu.eu4oa1w0 > button')
        close.click()
    except:
        pass

    time.sleep(1+random.random())

    # get the job data
    data=[]
    while True:
        try:

            jobcard=driver.find_element(By.XPATH,'//*[@id="mosaic-provider-jobcards"]').find_element(By.TAG_NAME,'ul')
            jobs=jobcard.find_elements(By.XPATH, './li')

            for job in jobs:
                try:
                    # get the job title, company, location, salary and job link
                    body=job.find_element(By.TAG_NAME,'tbody')
                    title=body.find_element(By.TAG_NAME,'a').find_element(By.TAG_NAME,'span').text
                    company=body.find_element(By.CSS_SELECTOR, 'span[data-testid="company-name"]').text
                    location=body.find_element(By.CSS_SELECTOR,'div[data-testid="text-location"]').text
                    salary="Not mentioned"
                    job_link=body.find_element(By.TAG_NAME,'a').get_attribute('href')

                    # get the salary if mentioned
                    try:
                        salary=body.find_element(By.CSS_SELECTOR, 'div.salary-snippet-container').text
                    except:
                        pass

                    # append the job data to the list
                    data.append({'title':title,'company':company,'location':location,'salary':salary,'job_link':job_link})
                # if any of the data is not found, skip the job
                except:
                    pass
        except NoSuchElementException:
            break
        
        time.sleep(2+random.random())

        # click on the next button
        try:
            next_button=driver.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]')
            next_button.click()
            time.sleep(1+random.random())
        
        # if the next button is not found, break the loop
        except NoSuchElementException:
            break

    # close the driver
    driver.quit()

    # return the job data
    return data



