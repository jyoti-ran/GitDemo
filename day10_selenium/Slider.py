from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
#driver.implicity_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider=driver.find_element(By.XPATH,"//body/div[2]/div[2]/span[1]")
max_slider=driver.find_element(By.XPATH,"//body/div[2]/div[2]/span[2]")

print("Location of sliders After moving .....")
print(min_slider.location)   # {'x': 59, 'y': 251}
print(max_slider.location)   # {'x': 613, 'y': 251}


act=ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print(min_slider.location)   # {'x': 59, 'y': 251}
print(max_slider.location)   # {'x': 613, 'y': 251} 

time.sleep(10)