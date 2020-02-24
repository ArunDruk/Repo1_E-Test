from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver import ActionChains

import time

driver=webdriver.Chrome()
# driver.get("http://www.msn.com")
# time.sleep(5)
# driver.maximize_window()
# ####################################################################################################
# # To open the link in new tab use below
# # driver.execute_script("window.open('http://www.yahoo.com','new window')")
# # driver.switch_to.window(driver.window_handles[1])
# ####################################################################################################
# driver.execute_script("window.open('http://www.yahoo.com', 'http://www.rediffmail.com','new window')")
# # If we give more than one URL's in the above line, the first url will open as a pop-up window and rest of the url's will not be opened.
# driver.switch_to_window(driver.window_handles[1])
# time.sleep(5)

driver.get("http://www.theTestingWorld.com/testings")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_name("fld_username").send_keys("Druk")
# ActionChains(driver).send_keys(Keys.TAB).perform() # To press special keys in keyboard like tab, shift, alt, control need to use Keys and import it
# ActionChains(driver).send_keys("Druk@gmail.com").perform() # To enter normal characters in keyboard just use ActionChains(driver).send_keys("abc").perform()
# to use special keys use "Keys. " or else for alphanumeric and special characters just send_keys("/")
time.sleep(3)
#act=ActionChains(driver)
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() # Ctrl+a operation, select all
# In Older version : ActionChains(driver).send_keys(Keys.CONTROL).send_keys("v").perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() # ctrl+c operation, copy it
ActionChains(driver).send_keys(Keys.TAB).perform()
time.sleep(5)
ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# In latest version this is changed you have to press keys_down and keys_up
time.sleep(10)
driver.quit()