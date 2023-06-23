import time

#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By

#serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
#driver=webdriver.Chrome(service=serv_obj)
#driver.implicitly_wait(10)

#driver.get("https://www.google.com/")
#driver.maximize_window()

#searchbox=driver.find_element(By.NAME,'q')
#searchbox.send_keys("selenium")
#searchbox.submit()

#time.sleep(5)
#driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a/h3").click()

#time.sleep(1000)













from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)  # seconds # implicity wait

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()













