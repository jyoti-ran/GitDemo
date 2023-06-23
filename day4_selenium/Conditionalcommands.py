
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed()   is_enabled()

searchbox=driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
#print("Display status:",searchbox.is_displayed())  # True
#print("Display status",searchbox.is_enabled())     # True


#is_selected()  - for radio button and check boxes

#maleradio_btn=driver.find_element(By.XPATH,"//*[@id='gender-male']")
#femaleradio_btn=driver.find_element(By.XPATH,"//*[@id='gender-female']")

#print(maleradio_btn.is_selected())   # False   (Both radio button's are not selected)
#print(femaleradio_btn.is_selected())  # False  (Both radio button's are not selected)

#maleradio_btn.click()  # using .click() method we selected male one then print it should return True
#print(maleradio_btn.is_selected())  # True

#femaleradio_btn.click()  # using .click() method we selected female one then print it should return True
#print(femaleradio_btn.is_selected())  #True


time.sleep(1000)



