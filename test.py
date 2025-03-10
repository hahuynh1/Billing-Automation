from selenium import webdriver  # interact with web browser
from selenium.webdriver.common.keys import Keys  # simulate key presses
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
# Replacing time.sleep() with WebDriverWait
dropdown_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'btn-menu') and .//span[contains(text(),'Health Plans')]]"))
)
dropdown_button.click()
 
# KF CHC button
KFchc_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "health-plans-menu-plan-kchc"))
)
KFchc_button.click()
 
# Eligibility Button
input("\nPress Enter to close the browser...")