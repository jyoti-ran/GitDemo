from selenium import webdriver

#For Chrome browser
#def headless_chrome():
    #from selenium.webdriver.chrome.service import Service
    #serv_obj = Service("C:\Drivers\chromesetup\chromedriver")
    #ops=webdriver.ChromeOptions()
    #ops.headless=True
    #driver=webdriver.Chrome(service=serv_obj,options=ops)
    #return driver


#For Edge browser
def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\Drivers\edgesetup\msedgedriver")
    ops=webdriver.EdgeOptions()
    ops.headless=True
    driver=webdriver.Edge(service=serv_obj,options=ops)
    return driver


#driver=headless_chrome()
driver=headless_edge()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()