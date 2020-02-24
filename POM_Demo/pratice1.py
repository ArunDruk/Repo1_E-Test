from selenium.webdriver import Chrome
import time
import pytest
from datetime import datetime

class Test_practicing:

    @pytest.fixture()
    def setup(self):
        self.driver = Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_verifyingTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        self.driver.get_screenshot_as_file("Orange_HRM.png")
        assert self.driver.title == "orangeHRM"  # OrangeHRM

    # @pytest.mark.hookwrapper
    # def pytest_runtest_makereport(item, call):
    #
    #     timestamp = datetime.now().strftime('%H-%M-%S')
    #
    #     pytest_html = item.config.pluginmanager.getplugin('html')
    #     outcome = yield
    #     report = outcome.get_result()
    #     extra = getattr(report, 'extra', [])
    #     if report.when == 'call':
    #
    #         feature_request = item.funcargs['request']
    #
    #         driver = feature_request.getfixturevalue('browser')
    #         driver.save_screenshot('D:/report/scr' + timestamp + '.png')
    #
    #         extra.append(pytest_html.extras.image('D:/report/scr' + timestamp + '.png'))
    #
    #         # always add url to report
    #         extra.append(pytest_html.extras.url('http://www.example.com/'))
    #         xfail = hasattr(report, 'wasxfail')
    #         if (report.skipped and xfail) or (report.failed and not xfail):
    #             # only add additional html on failure
    #             extra.append(pytest_html.extras.image('D:/report/scr.png'))
    #             extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
    #         report.extra = extra

# driver=Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# time.sleep(5)
# print(driver.title)
# driver.close()

# class Loginclass:
#     def __init__(self,driver):
#         self.driver=driver
#         driver=webdriver.Chrome()
#
#     def Login_method(self):
#         self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
#         self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
#         self.driver.find_element_by_id(self.login_button_id).click()



