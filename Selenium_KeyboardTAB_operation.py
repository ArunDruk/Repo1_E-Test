from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://www.theTestingWorld.com/testings")

time.sleep(4)
driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("ArunDruk")
driver.maximize_window()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys("arundruk@gmail.com").perform()

