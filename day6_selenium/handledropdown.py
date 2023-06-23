
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

dropcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
dropcountry=Select(dropcountry_ele)

# select option from the dropdown
#dropcountry.select_by_visible_text("India") # India       # Most of the time we use
#dropcountry.select_by_value("98")  # Iceland
#dropcountry.select_by_index(13)   # Australia


#cpature all the options and count the numbers
#alloptions=dropcountry.options
#print("total number of options: ",len(alloptions))   # it will show number of options and show in the console


#Capture all the options and print them
alloptions=dropcountry.options
print("total number of options: ",len(alloptions))

#for opt in alloptions:
 #   print(opt.text)         # it will print all the options and print it into the console



# select option from dropdown without using built-in method

#for opt in alloptions:
#    if opt.text=="India":
#        opt.click()
#        break



#if there is no select tag how we can deal with some other tag
alloptions=driver.find_elements(By.XPATH,"//*[@id='input-country']/option")
print(len(alloptions))




time.sleep(100)