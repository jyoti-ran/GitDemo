from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on the link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()


# find number of links in a page
#links=driver.find_elements(By.TAG_NAME,'a')      # using TAGNAME
links=driver.find_elements(By.XPATH,"//a")        # using XPATH
print("total number of links:",len(links))



# print all the link names in the console
#for link in links:
 #   print(link.text)







time.sleep(100)