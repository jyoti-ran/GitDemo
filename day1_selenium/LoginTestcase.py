# 1) Open web browser (Chrome/Firefox/Edge)
# 2) Open URL https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# 3) Enter username (Admin).
# 4) Enter password (admin123).
# 5) Click on Login.
# 6) Capture title of the home page. (Actual title)
# 7) Verify title of the home page: OrangeHRM (Expected)
# 8) Close browser

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

Actualtitle=driver.title
print(Actualtitle)
exp_title="OrangeHRM"

if Actualtitle==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Faieled")


time.sleep(10)