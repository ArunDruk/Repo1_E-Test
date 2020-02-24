from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

driver=webdriver.Chrome()
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.maximize_window()
driver.implicitly_wait(10)

# driver.find_element_by_xpath("//input[@ng-model='Email']").send_keys("arundruk@gmail.com")
# driver.find_element_by_xpath("//input[@ng-model='Password']").send_keys("")

# Not woeking
item_per_page=driver.find_element_by_xpath("//select[@ng-model='grid.options.paginationPageSize']")
time.sleep(5)
Select(item_per_page).select_by_value("number:30")
time.sleep(5)
eventFiringWebDriver=EventFiringWebDriver(driver).
eventFiringWebDriver.execute_script("document.querySelector('div[role=\"rowgroup\"][class*=\"ui-grid-viewport\"]').scrollTop=500")