from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

outer_frame=driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
driver.switch_to.frame(outer_frame)

innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Welcome")


driver.switch_to.parent_frame()  # directly switch to parent frame(outerframe)

time.sleep(5)