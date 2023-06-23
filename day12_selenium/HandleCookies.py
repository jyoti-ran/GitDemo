from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Capture Cookies from the browser
#print("size of cookies:",len(cookies))  #3

#print details of all cookies
#for c in cookies:
    #print(c)    # it will print all the cookies
    #print(c.get('name'),":",c.get('value'))   # it will print only name and value Attribute inside the key


#Add a new cookie to the browser
#driver.add_cookie({"name":"MyCookie","value":"123456"})
#cookies=driver.get_cookies()
#print("size of cookies after adding new one:",len(cookies))     #4


#Delete specific cookie from the browser
#driver.delete_cookie("MyCookie")
#cookies=driver.get_cookies()
#print("Size of cookies after deleted one:" ,len(cookies))   #3

#Delete all the cookies
driver.delete_all_cookies()   # Delete all the cookies
cookies=driver.get_cookies()
print("Size of cookies after deleted one:" ,len(cookies))    #0


driver.quit()