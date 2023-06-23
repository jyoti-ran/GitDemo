from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag & id css selector
# Tag is optional in all css selectors.
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc") #With tag and id
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("jyoti")  # without tag also its possible you can easily do.


#tag & class css selector
# Tag is optional in all css selectors.
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("jyooti@gmail.com") # some times spaces are not taken thats why after space remove all the part
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("jyooti@gmail.com")


#tag & attribute css selector
# You can take any attribute instead of name id
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("yelow@gmail.com")


#tag, class & attribute
# pass the value using tag, class & attribute in the password field with identifying
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("biswal@1234")


time.sleep(1000)