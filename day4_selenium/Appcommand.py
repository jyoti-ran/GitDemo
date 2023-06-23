 import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#print(driver.title)   # to know the title of the webpage
#print(driver.current_url)  # to know the url of the webpage
#print(driver.page_source)  # to know the source code of the webpage


time.sleep(1000)
driver.quit()
