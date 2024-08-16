import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Pageobjects.Loginpage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customerlogger import Loggen
from selenium.webdriver.common.keys import Keys
from testcases.conftest import setup
from testcases.conftest import pytest_configure
from testcases.conftest import pytest_metadata


import time


class Test001_Login:
    # We are getting this data fom - Utilities -readproperty.py
    baseURL = ReadConfig.getWebURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = Loggen.loggen()

    @pytest.mark.sanity
    def test_homepage_title(self, setup):
        self.logger.info("**************Test001_Login***********")
        self.logger.info("**************Verifying Homepage Title*****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(self.driver.title)
        if act_title == "Barbria":
            assert True
            self.logger.info("**************Homepage Title is passed*****************")
            self.driver.close()

        else:
            self.driver.save_screenshot("Screenshots/test_homepage_title.png")
            self.logger.error("**************Homepage Title is failed*****************")
            # self.driver.save_screenshot("test_homepage_title.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("**************Verifying Login Title*****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(self.driver.title)
        if act_title == "Barbria":
            assert True
            self.logger.info("**************Login Title is passed*****************")
            self.driver.close()

        else:
            self.driver.save_screenshot("Screenshots/test_login.png")
            self.logger.error("**************Login Title is failed*****************")
            self.driver.close()
            assert False
