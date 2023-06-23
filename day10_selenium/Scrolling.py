from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
#driver.implicity_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#1. Scroll down page by pixel

#driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return window.pageYOffset;")
#print("Number of pixels moved:",value)  # 3000


#2. scroll down page till the element is visible

#flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#value=driver.execute_script("return window.pageYOffset;")
#print("Number of pixels moved:",value)


#3. scroll down page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)


time.sleep(5)
#4. scroll up to starting position

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)


time.sleep(100)