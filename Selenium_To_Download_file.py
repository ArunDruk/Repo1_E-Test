import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# For downloading file, below additional steps
from selenium.webdriver.chrome.options import Options
chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{'download.default_directory':"E:\Download_path"})
driver=webdriver.Chrome(chrome_options=chromeOptions)
#Initialization of chromeOptions till above
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

driver.find_element_by_xpath("//input[@ng-model='FirstName']").send_keys("Arun")
time.sleep(2)
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys("Druk").perform()
driver.find_element_by_xpath("//textarea[@ng-model='Adress']").send_keys("California")
driver.find_element_by_xpath("//input[@ng-model='EmailAdress']").send_keys("arundruk@gmail.com")
driver.find_element_by_xpath("//input[@ng-model='Phone']").send_keys("+91-9986233833")
driver.find_element_by_xpath("//input[@value='Male']").click()
driver.find_element_by_xpath("//input[@value='Cricket']").click()
country_drp=Select(driver.find_element_by_id("countries"))
country_drp.select_by_visible_text("India")

time.sleep(4)
driver.find_element_by_xpath("//button[@id='submitbtn']").click()



