from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.flipkart.com/account/login?ret=%2Faccount%2Forders&fromMyOrdersPage=true")
driver.maximize_window()

#Login

driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/form/div[1]/input").send_keys("9090589188")
driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/form/div[2]/input").send_keys("Kahnu@1996")
driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/form/div[4]/button/span").click()
time.sleep(10)


#driver.find_element(By.XPATH,"//input[@name='q']").send_keys("mobile")
#driver.find_element(By.XPATH,"//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/button[1]/*[1]").click()
Electronics=driver.find_element(By.XPATH,"//body/div[@id='container']/div[1]/div[2]/div[1]/div[1]/span[1]")

#MouseHover
act=ActionChains(driver)

act.move_to_element(Electronics).click().perform()


time.sleep(10)



