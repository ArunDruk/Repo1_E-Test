#coding: latin-1
# -*- coding: latin-1 -*-
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://www.sic-info.org/en/services/lending/national-flags/")
driver.maximize_window()
time.sleep(4)
#driver.find_element_by_xpath("//a//span[text()='Português']").click()
driver.find_element_by_xpath("//li[@class='vi' and @lang='vi']").click()
time.sleep(4)
driver.find_element_by_xpath("//li[@class='services']//div[@class='parent']").click()