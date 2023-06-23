from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countryList=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

print(len(countryList))

for country in countryList:
    if country.text == "Japan":
        country.click()
        break

time.sleep(10)
