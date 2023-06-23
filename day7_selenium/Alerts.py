from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()



alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("jyoti")

alertwindow.accept()  # close alert window by using OK button
#alertwindow.dismiss()  # close alert window by using cancel button



time.sleep(15)

