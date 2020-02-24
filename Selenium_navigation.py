from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()

time.sleep(5)
driver.get("http://www.msn.com")
time.sleep(10)

driver.back() # presses back, previous page
time.sleep(5)

driver.forward() # presses forward icon
wait = WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable)