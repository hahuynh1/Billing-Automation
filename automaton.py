from selenium import webdriver # interact with web browser
from selenium.webdriver.common.keys import keys # simulate key presses

driver = webdriver.Chrome('./chromedriver')
driver.get("https://navinet.navimedix.com/eligibility-benefits/kchc/search#/")

print(driver.title)