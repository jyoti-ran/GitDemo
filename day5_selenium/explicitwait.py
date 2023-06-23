#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
#import time
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import ElementNotVisibleException
#from selenium.common.exceptions import ElementNotSelectableException
#from selenium.common.exceptions import Exception
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

#serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
#driver=webdriver.Chrome(service=serv_obj)

#mywait=WebDriverWait(driver,10)  # explicity wait declaration
#mywait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,
                                                  # ElementNotVisibleException,
                                                   #ElementNotSelectableException,
                                                  # Exception]
#                     )

#driver.get("https://www.google.com/")
#driver.maximize_window()

#searchbox=driver.find_element(By.NAME,'q')
#searchbox.send_keys("selenium")
#searchbox.submit()

#searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a/h3")))
#searchlink.click()

#driver.quit()
















from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

#mywait=WebDriverWait(driver,10) # explicit wait declaration   # VERY BASIC COMMAND BELOW MENTION COMMAND ARE THE ADAVANCED AND USING THIS WE CAN HEANDLE THE EXCEPTIONS IF THE ELEMENT IS NOT CORRECT WE CAN PROCEED WITH THE OTHER EXCEPTIONS.
mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException,
                                                   Exception]
                     )

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,'q')

searchbox.send_keys("selenium")
searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()


driver.quit()


























































