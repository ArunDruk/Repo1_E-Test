from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver=webdriver.Chrome()
# driver.get("https://www.quackit.com/html/codes/")
# time.sleep(10)


# driver.switch_to.frame("google_esf")
# driver.find_element_by_link_text("HTML Color").click()
# time.sleep(5)
#
# driver.switch_to_default_content()
# driver.find_element_by_link_text("Scripting").click()
# ###########################################################################################################
# #Scrolling the web page of flags and stopping at the position where the element is reached, taking the screenshot and
# # scrolling again to the end of the page.
# #Scrolling the methods:
# #driver.execute_script("arguments[0].scrollIntoView();",flag)
# #driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# ###########################################################################################################
driver.get("https://www.sic-info.org/en/services/lending/national-flags/")
driver.maximize_window()
time.sleep(15)

# Scroll till the element is visible, Denmark flag is Searched for:
flag=driver.find_element_by_xpath("//*[@id='mainInner']/section/div/ul[2]/li[26]/img")
driver.execute_script("arguments[0].scrollIntoView();",flag)
driver.save_screenshot("Mexi.png")
time.sleep(10)

# Scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")




###########################################################################################################
# # Automating a job application by entering values in the input boxes, selecting from drop_down, uploading file, clicking on check box / Radio button
###########################################################################################################
# driver.get("http://careers.edgeindia.com/job-details.php?req_id=1436")
# driver.maximize_window()
# driver.find_element_by_name("apply").click()
# time.sleep(3)
#
# #selecing from the drop down using "select_by_visible_text" (other methods select_by_index, select_by_value)
# Gender_dd=Select(driver.find_element_by_id("cboGender"))
# Gender_dd.select_by_visible_text("Male")
#
# # Entering values in input boxes
# driver.find_element_by_id("txtName").send_keys("Arun S Kumar")
# driver.find_element_by_id("txtEmail").send_keys("arundruk@gmail.com")
# driver.find_element_by_id("txtMobile").send_keys("+91-9738476056")
# driver.find_element_by_id("txtCompany").send_keys("OTSI")
#
# #selecing from the drop down
# Current_location_DD=Select(driver.find_element_by_id("txtLocation"))
# Current_location_DD.select_by_visible_text("Bangalore")
#
# Select(driver.find_element_by_id("PreferredLocation")).select_by_visible_text("Bangalore")  # Selecting in a single line instead of taking into a Class Select variable
# Select(driver.find_element_by_id("experience")).select_by_visible_text("9")
#
# #uplaoding a file, make sure you use forward slash for the path
# upload_path="C:/Users/Admin/Desktop/Resumes/Resume.docx"
# driver.find_element_by_id("cvfile").send_keys(upload_path)
#
# #Working on radio buttons and check boxes, two methods are available is_selected() and click()
# status=driver.find_element_by_id("nacv").is_selected()
# print(status)
#
# driver.find_element_by_id("nacv").click()
#
# status=driver.find_element_by_id("nacv").is_selected()
# print(status)
###########################################################################################################

###########################################################################################################
# Working, Opening multiple tabs by using a loop for the click element and switching to each tab and doing operations.
###########################################################################################################
# driver.get("http://www.msn.com")
# driver.maximize_window()
# news_element=driver.find_element_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/ul/li[2]/a")
# for i in range(1,5):
#     ActionChains(driver).key_down(Keys.CONTROL).click(news_element).key_up(Keys.CONTROL).perform()
#
# Handles=driver.window_handles
#
# driver.switch_to_window(Handles[4])
# driver.get("http://support.microsoft.com")
# time.sleep(5)
#
# driver.switch_to_window(Handles[3])
# driver.get("http://www.yahoo.com")
# time.sleep(5)
#
# driver.switch_to_window(Handles[2])
# driver.get("http://www.tamilmatrimony.com")
# time.sleep(5)
#
# driver.switch_to_window(Handles[0])
# time.sleep(5)
#driver.close()
###########################################################################################################
time.sleep(15)
driver.quit()