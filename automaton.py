from selenium import webdriver # interact with web browser
from selenium.webdriver.common.keys import Keys # simulate key presses\
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import login
import time

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://navinet.navimedix.com/#/")

# LOGIN PAGE
username = driver.find_element(By.ID, "LoginPortletUsername")
password = driver.find_element(By.ID, "LoginPortletPassword")

username.send_keys(login.USERNAME)
password.send_keys(login.PASSWORD)

login_button = driver.find_element(By.ID, "submitButton")
login_button.click()

print(driver.current_url)

# NAVIGATE TO CLIENT ID INPUT
# Health Plans dropdown
time.sleep(3)
HP_button = driver.find_element(By.XPATH, "//span[contains(text(),'Health Plans')]")
HP_button.click()

# KF CHC button
time.sleep(1)
KFchc_button = driver.find_element(
    By.ID, "health-plans-menu-plan-kchc" 
)
KFchc_button.click()

# Eligibility Button
time.sleep(1)
eligibility_button = driver.find_element(
    By.XPATH, 
    "//a[@href='/eligibility-benefits/kchc/search']"
)
eligibility_button.click()

input("\nPress Enter to close the browser...")

