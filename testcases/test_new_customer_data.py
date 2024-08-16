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
import random
import string
from Pageobjects.New_customer import newly_added_customers


class Test003_Login:
    # We are getting this data fom - Utilities -readproperty.py
    baseURL = ReadConfig.getWebURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = Loggen.loggen()

    @pytest.mark.regression
    def test_new_customer_data(self, setup):
        self.logger.info("**************Test003_begins*****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        print(self.driver.title)
        self.nc = newly_added_customers(self.driver)
        time.sleep(5)
        self.nc.clickdashboard()
        time.sleep(3)
        self.nc.clickhome()
        time.sleep(2)
        self.nc.clickcustomer()
        time.sleep(2)
        self.nc.clickAdd_new_customer()
        time.sleep(2)
        self.fullname = ((random.choice(string.ascii_letters.upper()) + random.choice(
            string.ascii_letters.lower()) + random.choice(string.ascii_letters.lower()) + random.choice(
            string.ascii_letters.lower())))
        print(self.fullname)
        self.nc.setFullname(self.fullname)
        self.nc.clickgender()
        self.email = ((random.choice(string.ascii_letters.lower()) + random.choice(
            string.ascii_letters.lower()) + random.choice(string.ascii_letters.lower()) + random.choice(
            string.ascii_letters.lower())) + "@mailinator.com")
        print(self.email)
        self.nc.setCustomeremail(self.email)
        self.lower_limit = 8000000000
        self.upper_limit = 9999999999
        self.phonenumber = (random.randint(self.lower_limit, self.upper_limit))
        print(self.phonenumber)
        self.nc.setphonenumber(self.phonenumber)
        self.nc.clickcustomeraddbutton()
        self.logger.info("**************New customer has been added*****************")
        time.sleep(3)
        self.msg = self.driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div").text
        print(self.msg)
        if 'Client created successfully' in self.msg:
            assert True
            self.logger.info("**************customer has been added successfully*****************")
        else:
            self.driver.save_screenshot("Screenshots/test_003.png")
            self.logger.error("**************Adding customer is failed*****************")
            assert False
        time.sleep(2)
        self.lp.clickTV()
        self.lp.clickLogout()
        self.driver.close()
        self.logger.info("**************End of Add Customer Testcase*****************")
