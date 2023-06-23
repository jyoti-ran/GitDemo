from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj,options=ops)



driver.get("https://whatmylocation.com/")
driver.maximize_window()

time.sleep(12)



