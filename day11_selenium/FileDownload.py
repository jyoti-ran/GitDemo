import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location=os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromesetup\chromedriver")
    
#download files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver



driver=chrome_setup()

driver.get("https://www.theice.com/market-data/desktop-solutions/ice-connect/excel-addin-templates/download")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'Download ICE XL')]").click()



time.sleep(100)




