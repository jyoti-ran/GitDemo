from selenium import webdriver
import time
import os

from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()
#reglink=Keys.CONTROL+Keys.RETURN
#driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)



#NEW Tab - Selenium4 : Opens a new tab and switches to new tab
#driver.get("https://www.opencart.com/")
#driver.maximize_window()
#driver.switch_to.new_window('tab')
#driver.get("https://www.orangehrm.com/")


#New Window - Selenium4 :  Opens a new browser window and switches to new window
#driver.get("https://www.opencart.com/")
#driver.switch_to.new_window('window')
#driver.get("https://www.orangehrm.com/")

time.sleep(100)


