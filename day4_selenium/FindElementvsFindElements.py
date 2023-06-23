import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

# find_element() - Returns single webelement

# Locators matching with the single webelement

#element=driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
#element.send_keys("jyoti")

elements=driver.find_elements(By.XPATH,"/html/body/div[6]/div[4]/div[1]//a")
print(len(elements)) # 22 link are there in the footer section
#print(elements[0].text)

for i in elements:
    print(i.text)

time.sleep(1000)