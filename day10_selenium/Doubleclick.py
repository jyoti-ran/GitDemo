from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult")   # switch to frame

field1=driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")

button=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")

act=ActionChains(driver)
act.double_click(button).perform() # double click action on the element

time.sleep(10)