import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose")
driver.maximize_window()

#Absolute xpath

#driver.find_element(By.XPATH,"/html/body/div[3]/div/div/section[1]/div[2]/div/div/div/div/form/div/input").send_keys("thirts@gmail.com")
#driver.find_element(By.XPATH,"/html/body/div[3]/div/div/section[1]/div[2]/div/div/div/div/form/div/button").click()
#driver.find_element(By.XPATH,"/html/body/div[3]/div/div/section[2]/div/div/div/div/div[2]/form/fieldset/div[1]/div/input").send_keys("jyoti ranjan biswal")
#driver.find_element(By.XPATH,"/html/body/div[3]/div/div/section[2]/div/div/div/div/div[2]/form/fieldset/div[2]/div/input").send_keys("Ranjan biswal")
#driver.find_element(By.XPATH,"/html/body/div[3]/div/div/section[2]/div/div/div/div/div[2]/form/fieldset/div[4]/div/input").send_keys("9438475943")
#driver.find_element(By.XPATH,"/html/body/div[3]/div/div/section[2]/div/div/div/div/div[2]/form/fieldset/div[5]/div/select").send_keys("Albania")



#Relative xpath

#driver.find_element(By.XPATH,"//*[@id='myText']").send_keys('jyoti@gmail.com')
#driver.find_element(By.XPATH,"//button[@id='linkadd']").click()

# Self
#text_msg=driver.find_element(By.XPATH,"//a[normalize-space()='HUDCO']/self::a").text
#print(text_msg)  # HUDCO

# Parent
#text_msg=driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[3]/td[1]/a/parent::td").text
#print(text_msg)  # Mazagon Dock Ship

# child
#childs=driver.find_elements(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/ancestor::tr/child::td")
#print(len(childs))  # 5

# Ancestor
#text_msg=driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/ancestor::tr").text
#print(text_msg)  # Garden Reach Ship A 474.65 515.85 + 8.68  #  Entire row data will printed


# Descendant
#descendents=driver.find_elements(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[6]/td[1]/a/ancestor::tr/descendant::*")
#print("Number of descendant nodes:",len(descendents))    # Number of descendant nodes: 7


# following
descendents=driver.find_elements(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[6]/td[1]/a/ancestor::tr/following::*")


time.sleep(1000)

