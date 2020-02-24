import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import os
import wget
import random
import string
#url="http://jvcorp-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/linkedin.png"
#filename=url.split("/")[-1]
#urllib.request.urlretrieve(url,"E:\Test\Downloaded_images"+filename)
#filename1=re.search(r'/\.*',url) #search in the url string and extract the filename as .png
#os.system(wget filename url)
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("arun") # Google search and entering vlue "arun"
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()# Click on Google Search button
time.sleep(5)
Gmap_element=driver.find_element(By.XPATH,"//*[@id='hdtb-msb-vis']/div[2]/a")
ActionChains(driver).key_down(Keys.CONTROL).click(Gmap_element).key_up(Keys.CONTROL).perform()
time.sleep(10)
# ActionChains(driver) \
#     .key_down(Keys.CONTROL) \
#     .click(Gmap_element) \
#     .key_up(Keys.CONTROL) \
#     .perform()
#
# #time.sleep(10)
#new_tab_element=driver.find_element(By.TAG_NAME,"body")
#ActionChains(driver).key_down(Keys.CONTROL).click(new_tab_element).key_up(Keys.CONTROL).perform()
#ActionChains(driver).key_down(Keys.CONTROL).send_keys("T").key_up(Keys.CONTROL).perform()
#Handles=driver.window_handles
# print(type(Handles))
#driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND + Keys.NUMPAD2)

#driver.switch_to_window(Handles[1])
#driver.get("https://yahoo.com")

#driver.find_element(By.TAG_NAME,"body").send_keys(Keys.CONTROL+'t')
#ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
#

#
# for handle in Handles:
#     print(handle, driver.title)



#driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()
# cookies=driver.get_cookies()
# print(len(cookies))
# print(cookies)

# # Selenium tutorial headings in a text file.
# #driver.get("https://www.youtube.com/playlist?list=PLUDwpEzHYYLvx6SuogA7Zhb_hZl3sln66")
# links=driver.find_elements(By.PARTIAL_LINK_TEXT,"Selenium with Python")
#
# with open("Selenium_tutorial_python_links.txt",'w') as fw:
#     for link in links:
#         fw.write(link.text + "\n")

#time.sleep(10)
# # Downloading the image
# images=driver.find_elements(By.TAG_NAME,"img")
# print(type(images))
# a=len(images)
# chars=string.ascii_letters
# filename= list(random.choice(chars) for i in range(1,a+1))
# for image in images:
#     #image_link=image.get_attribute("src")
#     #filename=image_link.split('/')[-1]
#     #filepath="E:\Test\DownloadedImages" + filename
#     i=1
#     urllib.request.urlretrieve(image.get_attribute("src"), filename[i])
#     i+=1

    #print(image.get_attribute("src"))

# # To take the screenshot
# driver.save_screenshot("screenshot.png")
# # To collect all the links in a website using the tag_name as 'a' and get_attribute('href')
# links=driver.find_elements(By.TAG_NAME,'a')
# with open("w3_links.txt",'w') as fw:
#     for link in links:
#         fw.write(link.get_attribute('href') +"\n")
time.sleep(15)
driver.quit()

