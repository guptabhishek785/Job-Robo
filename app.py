
# Immporting necessary dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Evidence import evidence
import time
import datetime

# Creating an instance of a chrome driver
file_path = 'your_path'
driver = webdriver.Chrome(executable_path='PATH_TO_CHROMEDRIVER')
time.sleep(2)

# Wait for the form fields to be visible and interactable
wait = WebDriverWait(driver, 10)


# Loading the website to automate
driver.get('https://www.tesla.com/careers/search/job/apply/')

# Application with each steps for each field sorted page wise

# Page 1
wait.until(EC.element_to_be_clickable((By.NAME, "personal.firstName"))).send_keys('_______')
wait.until(EC.element_to_be_clickable((By.NAME, "personal.lastName"))).send_keys('_______')
wait.until(EC.element_to_be_clickable((By.NAME, "personal.phone"))).send_keys('_______')
wait.until(EC.element_to_be_clickable((By.NAME, "personal.phoneType"))).send_keys('_______', Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.NAME, "personal.email"))).send_keys('_______')
wait.until(EC.element_to_be_clickable((By.NAME, "personal.country"))).send_keys('_______', Keys.ENTER)
driver.execute_script("window.scrollBy(0, 450)")
wait.until(EC.element_to_be_clickable((By.NAME, "personal.profileLinks[0].link"))).send_keys('_______')
wait.until(EC.element_to_be_clickable((By.NAME, "personal.profileLinks[0].type"))).send_keys('Linkedin', Keys.ENTER)
driver.execute_script("window.scrollBy(0, 450)")
wait.until(EC.element_to_be_clickable((By.NAME, "personal.evidenceOfExcellence"))).send_keys(evidence)
time.sleep(1)
driver.execute_script("window.scrollBy(0, 450)")
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@accept='.pdf,.doc,.docx,.txt' and @class='tds-form-input-file-upload']"))).send_keys(file_path)
wait.until(EC.element_to_be_clickable((By.NAME, "next"))).click()
time.sleep(1)


# Page 2
wait.until(EC.element_to_be_clickable((By.NAME, "legal.legalNoticePeriod"))).send_keys("Immediately", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="legal.legalImmigrationSponsorship"][value="yes"]'))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="legal.legalConsiderOtherPositions"][value="yes"]'))).click()
driver.execute_script("window.scrollBy(0, 500)")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="legal.legalFormerTeslaEmployee"][value="no"]'))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="legal.legalFormerTeslaInternOrContractor"][value="no"]'))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="legal.legalReceiveNotifications"][value="yes"]'))).click()
driver.execute_script("window.scrollBy(0, 900)")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="legal.legalAcknowledgment"][value="false"]'))).click()
wait.until(EC.element_to_be_clickable((By.NAME, "legal.legalAcknowledgmentName"))).send_keys("_______")
time.sleep(0.5)
wait.until(EC.element_to_be_clickable((By.NAME, "next"))).click()
time.sleep(3)


# Page 3
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="eeo.eeoAcknowledgment"][value="false"]'))).click()
wait.until(EC.element_to_be_clickable((By.NAME, "eeo.eeoGender"))).send_keys("Male", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.NAME, "eeo.eeoVeteranStatus"))).send_keys("I am not a veteran", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.NAME, "eeo.eeoRaceEthnicity"))).send_keys("Asian", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.NAME, "eeo.eeoDisabilityStatus"))).send_keys("No", Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.NAME, "eeo.eeoDisabilityStatusName"))).send_keys("_______")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='tds-btn' and @type='submit']"))).click()

time.sleep(2)
 
