from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_ele=driver.find_element(By.ID,"box6")

target_ele=driver.find_element(By.ID,"box106")


act=ActionChains(driver)

act.drag_and_drop(source_ele,target_ele).perform()    # drag and drop operation

time.sleep(10)