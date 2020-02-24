###########################################################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
driver=webdriver.Chrome() #Driver already placed in C:\Users\Admin\AppData\Local\Programs\Python\Python37-32\Scripts
###########################################################################################################
# # #Opening a URL and finding how many links are available in that and printing the link names
# driver.get("https://www.google.com/search?rlz=1C1CHBD_enIN871IN871&sxsrf=ACYBGNTLAYeuMVFpm7PL9Fhp1TU_UkiEXw%3A1576336819329&ei=s_30XcXtE-uR4-EP_42v8AQ&q=how+to+find+driver+find+element+in+naukri.com&oq=how+to+find+driver+find+element+in+nau&gs_l=psy-ab.3.0.33i160l2.11334.33721..35431...13.0..0.197.7368.0j50......0....1..gws-wiz.....10..35i39j0i7i30j0j0i30j0i333j0i5i30j35i362i39j0i273j0i131j0i67j0i20i263j33i22i29i30j0i22i30.aPfpfP7AoS0")
# #driver.find_element_by_class_name("LC20lb").click()
# links=driver.find_elements(By.CLASS_NAME,"LC20lb") #CLASS_NAME attribute remains same for all the links.
# print(type(links),len(links))
# for link in links:
#     print(link.text)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Pune").click() #By using "PARTIAL_LINK_TEXT" any name which is part of the link you can give but case-sensitive.
# print(driver.title)
###########################################################################################################
# driver.get("http://newtours.demoaut.com/")
driver.get("https://www.naukri.com/mnjuser/homepage")
driver.find_element(By.ID,"usernameField").send_keys("arundruk@gmail.com")
time.sleep(5)
driver.find_element(By.ID,"passwordField").send_keys("Sep@2019")
time.sleep(5)
driver.find_element(By.TAG_NAME,"button").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Comviva").click()
time.sleep(10)
driver.quit()
