from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("http://thetestingworld.com")

# Mouse Move-Hover Operation.
TRAINING=driver.find_element_by_xpath("//*[@id='menu531']/span")
time.sleep(2)
CORPORATE_TRAINING=driver.find_element_by_xpath("//*[@id='menu532']/span")
time.sleep(2)
click_element=driver.find_element_by_xpath("//*[@id='menu536']/span")
time.sleep(2)
# Below is the mouse hover operation.
ActionChains(driver).move_to_element(TRAINING).move_to_element(CORPORATE_TRAINING).move_to_element(click_element).click().perform()

# Below is the Mouse Right click operation.
ActionChains(driver).context_click().perform()