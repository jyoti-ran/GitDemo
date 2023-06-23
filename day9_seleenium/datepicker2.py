from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#Date of birth element

driver.find_element(By.XPATH,"//input[@id='dob']").click()  # opens date picker element

# capturing month & year

datepicker_month=driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
datepicker_month1=Select(datepicker_month)
datepicker_month1.select_by_visible_text("Dec")  # month is got selected from dropdown

driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
datepicker_year=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
datepicker_year.select_by_visible_text("1990")


# capturing dates
alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")


for date in alldates:
    if date.text=="25":
        date.click()
        break


time.sleep(100)