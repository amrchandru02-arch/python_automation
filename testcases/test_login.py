import pytest
from selenium import webdriver
import os
from pageobject.login_page import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_Login:
    BaseURL = ReadConfig.getApplicationurl()
    username = ReadConfig.getApplicationusername()
    password = ReadConfig.getApplicationpassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def HomePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.BaseURL)
        actual_title = self.driver.title

        if actual_title == "nop demo store. Login":
            assert True
            screenshot_dir = ".\\Screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            self.driver.save_screenshot(
                os.path.join(screenshot_dir, "HomePageTitle.png")
            )
        else:
            assert False

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()



