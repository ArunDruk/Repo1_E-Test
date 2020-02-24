import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os


#driver=webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win2\chromedriver")
driver=webdriver.Chrome()
###########################################################################################################
#Gmail Account login and logout
passwd=os.environ.get("my_passwd")
driver.get("http://mail.google.com")
driver.maximize_window()
driver.find_element_by_id("identifierId").send_keys("arundruk")
time.sleep(2)
driver.find_element_by_id("identifierNext").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@name='password']").send_keys(passwd)
driver.find_element_by_id("passwordNext").click()
time.sleep(5)
#driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a").click()
driver.find_element_by_xpath("//a[@class='gb_D gb_Oa gb_i']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='gb_71']").click()
time.sleep(5)
driver.close()
###########################################################################################################
# driver.get("https://www.jobvite.com/")
# # # Open the URL and download all the images link present in the URL into a text file
# # images=driver.find_elements(By.TAG_NAME,"img")
# # for image in images:
# #     urllib.request.urlretrieve(image.get_attribute('src')+"\n","E:\Test\Downloaded_images")
#
# def func():
#     print("Just to check some variable value ..")
#     print("__name__ is",__name__)
# # saving the images link in a text file "Images1.txt"
# # with open("Images1.txt",'w') as fw:
# #     for image in images:
# #         fw.write("\n"+image.get_attribute('src'))
#
# ###########################################################################################################
# # Finding the number of clickable links in the URL ""https://www.jobvite.com/" and writing it to text file "jobinvite_contents.txt"
# # driver.find_element_by_xpath("//*[@id='menu-main-menu-simple']/li[3]/a").click()
# # driver.find_element(By.PARTIAL_LINK_TEXT,"Candidate Engagement").click()
#
# # lists=driver.find_elements(By.TAG_NAME,"a")
# # print(len(lists))
# #
# # with open("jobinvite_contents.txt",'w') as fw:
# #     for list in lists:
# #         fw.write(list.text +"\n")
# if __name__=="__main__":
#     print(func())
#
# time.sleep(3)
# driver.close()