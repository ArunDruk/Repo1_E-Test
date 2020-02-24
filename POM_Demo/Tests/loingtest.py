from selenium import webdriver
import sys
sys.path.append("E:\Test\POM_Demo")
from


import pytest
# from POM_Demo.Pages.loginpage import LoginPage
# from POM_Demo.Pages.homepage import HomePage
from POM_Demo.Utils import  utils
import allure
import moment

print(sys.path)

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/Users/Administrator/PycharmProjects/AutomationFramework_1/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("There was an exception")

            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "C:/Users/Administrator/PycharmProjects/AutomationFramework_1/screenshots/" + screenshotName + ".png")

            raise

        else:
            print("No exceptions occurred")

        finally:
            print("I am inside finally block")