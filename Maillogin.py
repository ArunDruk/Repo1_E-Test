from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

driver=webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win2\chromedriver")
#driver=webdriver.Ie(executable_path="E:\Drivers\IEDriverServer_Win32_3.14.0\IEDriverServer")
driver.get("http://mail.google.com")
#driver.maximize_window()
driver.find_element_by_id("identifierId").send_keys("arundruk")
time.sleep(2)
driver.find_element_by_id("identifierNext").click()
time.sleep(3)
# driver.find_element_by_name("password").send_keys("Jan@2019") #Inputting by attribute name
#driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Jan@2019")
password=os.environ.get("my_passwd")
print(password)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_id("passwordNext").click()
driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='gb_71']").click()
time.sleep(5)
#driver.find_element_by_xpath("//*[@class='aAU']").click()
#time.sleep(5)
driver.close()