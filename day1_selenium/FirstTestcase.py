#id  : driver.find_element(By.ID,"mention the id").send_keys("If you want to send any value to that particular item")
#name : driver.find_element(By.NAME,"mention the name").send_keys("If you want to send any value to that particular name attribute you can share")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#   id & name locators
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#Linktext & partial linktext
#<a href="/register?returnUrl=%2Fsearch%3Fq%3DLenovo%2BThinkpad%2BX1%2BCarbon%2BLaptop" class="ico-register">Register</a> #(Here we can find out using linktext)
#driver.find_element(By.LINK_TEXT,"Register").click()  # Performing the action using Linktext
#driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click() # Using partial_link_text if we can specify some part it will work


#using the class locators

#slider=driver.find_elements(By.CLASS_NAME,'list')
#print(len(slider))


#using the Tagname locators

sliders=driver.find_elements(By.TAG_NAME,'a')
print(len(sliders))




time.sleep(1000)
