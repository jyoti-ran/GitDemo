from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  # switch to frame

#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("07/30/2022")   #mm/dd/yyyy


year="2027"
month="April"
date="30"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click() # opens datepicker

#select  month & year

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #Next arrow
        #driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()  #previous arrow

#select date

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break



time.sleep(10)
