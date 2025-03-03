from selenium import webdriver # interact with web browser
from selenium.webdriver.common.keys import Keys # simulate key presses\
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import login

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://navinet.navimedix.com/#/")

username = driver.find_element(By.ID, "LoginPortletUsername")
password = driver.find_element(By.ID, "LoginPortletPassword")

username.send_keys(login.USERNAME)
password.send_keys(login.PASSWORD)

login_button = driver.find_element(By.ID, "submitButton")
login_button.click()

print(driver.current_url)



input("\nPress Enter to close the browser...")

