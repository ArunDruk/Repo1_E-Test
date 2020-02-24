#from selenium import webdriver
import time
from selenium.webdriver import Chrome
driver=Chrome()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")
time.sleep(3)

buyers=driver.find_elements_by_xpath("//div[@title='buyer-name']")
prices=driver.find_elements_by_xpath("//span[@class='item-price']")

for i in range(len(buyers)):
    print(buyers[i].text + " : " + prices[i].text)

time.sleep(7)
driver.close()