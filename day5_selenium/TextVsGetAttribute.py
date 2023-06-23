from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/login")

#emailbox=driver.find_element(By.XPATH,"//*[@id='Email']")


#emailbox.clear()
#emailbox.send_keys("lata321@gmail.com")


#print("result of text:",emailbox.text)
#print("result of get_attribute():",emailbox.get_attribute('value'))

button=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button")
print("result of text:",button.text)
print("result of get_attribute():",button.get_attribute('value'))

time.sleep(1000)