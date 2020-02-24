import pytest
from selenium import webdriver
import time

#global driver

class Test_OrangeHRM():
    # global driver
    @pytest.fixture#(scope='session')
    def setup(cls):
        #global driver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        # time.sleep(5)
        # yield
        # cls.driver.quit()

    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

    def test_logout(cls):
       # driver = self.driver
        time.sleep(5)
        cls.driver.find_element_by_id("welcome").click()
        time.sleep(3)
        cls.driver.find_element_by_link_text("Logout").click()
        time.sleep(3)
        cls.driver.quit()
