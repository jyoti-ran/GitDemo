import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH,"//div[contains(text(),'Upload Resume')]").click()
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:\Users\sample.pdf")

time.sleep(10)
