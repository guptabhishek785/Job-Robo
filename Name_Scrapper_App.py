
## Import Dependencies
import pandas as pd
from collections import defaultdict 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## Enter your Login Details
email = 'your_email'
password = 'your_password'  


## Creating an instance of Chrome Browser
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
time.sleep(1)


# Loading the website and logging in
driver.get('https://www.linkedin.com/')
driver.find_element(By.XPATH,'//*[@id="session_key"]').send_keys(email)
driver.find_element(By.XPATH,'//*[@id="session_password"]').send_keys(password, Keys.ENTER)

## Entering the find field and selecting "People"
find_input = "Tesla Recruiters"
temp = driver.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input')
time.sleep(1)
temp.send_keys(find_input)
time.sleep(1)
temp.send_keys(Keys.DOWN, Keys.ENTER)
recruiter_list = []

## Main scraping starts here

# Rerun from here for more names
for x in range(5):
    pg = driver.find_elements(By.CLASS_NAME,'app-aware-link')
    for p in pg:
        r = p.text.split(' ')[:2]
        if len(r) > 1:
            if '\n' in r[-1]:
                r[-1] = r[-1].replace("\nView","")
                recruiter_list.append(r) 
    time.sleep(4)
    driver.execute_script("window.scrollBy(0, 1050)")
    time.sleep(2)
    button = driver.find_element(By.CSS_SELECTOR,"button[aria-label='Next']")
    button.click()
    time.sleep(2)

# Printing the list
print(recruiter_list)
print(len(recruiter_list))


## Converting the list into excel sheet
recruiter_list = pd.DataFrame(recruiter_list)
# recruiter_list.to_excel(find_input+'.xlsx', index = False)
recruiter_list.to_excel('Rivian_recruiter.xlsx', index = False)

 