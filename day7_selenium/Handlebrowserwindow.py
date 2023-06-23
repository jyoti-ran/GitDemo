from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromesetup\chromedriver")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://www.instagram.com/")
driver.maximize_window()


#To know single window id
#windowid=driver.current_window_handle
#print(windowid) # CDwindow-69AEE3320907C258B8525F5117F95B5C
                # CDwindow-239EC3E6342028BF8F6793C8F3E51FA8  (Every time you check the new windowid will be generated)


driver.find_element(By.LINK_TEXT,"Meta").click()
windowsIDs=driver.window_handles


#Approach 1 (If you have just 1 or 2 window then we can menage in this way)


#parentwindowid=windowsIDs[0]   # CDwindow-AE460EDFA635DED676168F4B6B7710A3
#childwindowid=windowsIDs[1]    # CDwindow-091E6759842E15E1600449FC7E105AA4

#print(parentwindowid,childwindowid)

#driver.switch_to.window(childwindowid)
#print("title of the child window",driver.title)


#driver.switch_to.window(parentwindowid)
#print("title of the parent window:",driver.title)




#Approach 2 (If you have multiple window we can menage through for loop)

time.sleep(3)

for winid in windowsIDs:
    driver.switch_to.window(winid)
    print(driver.title)
    if driver.title=="Instagram":
        driver.close()



