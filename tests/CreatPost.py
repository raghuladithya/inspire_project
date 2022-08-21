from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import allure
from Utils import utils as utils
from Pages.LoginPage import LoginPage
from Pages.CreatPostPage import CreatePost


@pytest.mark.usefixtures("test_setup")
class Testadvancedtracking():

    def test_login(self):
        browser = self.browser
        browser.get(utils.URL)
        time.sleep(5)

        login = LoginPage(browser)
        login.click_signin()
        time.sleep(5)
        allure.attach(self.browser.get_screenshot_as_png(), name="login", attachment_type=allure.attachment_type.PNG)
        login.enter_username(utils.Username)
        allure.attach(self.browser.get_screenshot_as_png(), name="username", attachment_type=allure.attachment_type.PNG)
        login.enter_password(utils.Password)
        allure.attach(self.browser.get_screenshot_as_png(), name="Password", attachment_type=allure.attachment_type.PNG)
        login.click_login()
        time.sleep(5)

    def test_creatpost(self):
        browser = self.browser
        createpost = CreatePost(browser)
        createpost.click_createpost()
        allure.attach(self.browser.get_screenshot_as_png(), name="Advancetracking", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        createpost.click_plusbutton()
        allure.attach(self.browser.get_screenshot_as_png(), name="Advancetracking",attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        createpost.click_topics()
        allure.attach(self.browser.get_screenshot_as_png(), name="Advancetracking",attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        createpost.enter_title(utils.title)
        allure.attach(self.browser.get_screenshot_as_png(), name="trackingnumber", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        createpost.enter_body(utils.body)
        allure.attach(self.browser.get_screenshot_as_png(), name="trackingnumber",attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        advancetracking.click_postbutton()
        allure.attach(self.browser.get_screenshot_as_png(), name="search", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def test_logout(self):
        browser = self.browser
        homePage = Homepage(browser)
        homePage.click_logout()

