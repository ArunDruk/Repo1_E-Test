from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("http://www.msn.com")
time.sleep(5)
driver.maximize_window()
# ####################################################################################################
# # To open the link in new tab use below
driver.execute_script("window.open('http://www.yahoo.com','new window')")
driver.switch_to.window(driver.window_handles[1])
# ####################################################################################################
# driver.execute_script("window.open('http://www.yahoo.com', 'http://www.rediffmail.com','new window')")
# # If we give more than one URL's in the above line, the first url will open as a pop-up window and rest of the url's will not be opened.
# driver.switch_to_window(driver.window_handles[1])
# time.sleep(5)