from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1) select specific checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()  # clicking one check boxes

#here 7 checkboxes are there


# number of checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#print(len(checkboxes))



#Approach 1  range function using for loop selecting all checkbox
#for x in range(len(checkboxes)):
#    checkboxes[x].click()


#Approach 2 range function using for loop selecting all checkbox
#for checkbox in checkboxes:
#   checkbox.click()


# selecting multiple checkboxes by choice
#for checkbox in checkboxes:
 #   weekname = checkbox.get_attribute('id')
  #  if weekname=='monday' or weekname=='tuesday':
   #     checkbox.click()



#According to our scenario we want to select the last 2 checkboxes
#for i in range(len(checkboxes)-2,len(checkboxes)):
#    checkboxes[i].click()




#According to our scenario we want to select last 1 checkboxes
#for i in range(len(checkboxes)-1,len(checkboxes)):
 #   checkboxes[i].click()


#Selecting first 2 checkboxes
#for i in range(len(checkboxes)):
#    if i<2:
#        checkboxes[i].click()


#time.sleep(10)
#clearing all the checkboxes in one short
#for checkbox in checkboxes:
 #   if checkbox.is_selected():
  #     checkbox.click()








time.sleep(100)