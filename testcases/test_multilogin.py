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
# from testcases import conftest
import testcases
from utilities import XLUtils
import openpyxl
import time
from openpyxl import load_workbook


class Test_Multilogin():
    # We are getting this data fom - Utilities -readproperty.py
    baseURL = ReadConfig.getWebURL()
    path = ".//Testdata/LoginData.xlsx"
    logger = Loggen.loggen()

    @pytest.mark.regression
    def test_login_multilogin(self, setup):
        self.logger.info("************** Test-002-Verifying Multilogin*****************")
        self.logger.info("**************Multilogin test starts*****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in an excel:", self.rows)
        lst_status = []  # Empty array list

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            print(self.driver.title)
            exp_title = "Barbria"
            if act_title == exp_title:
                self.logger.info("*****Passed********")
                if self.exp == "Pass":
                    self.logger.info("*********Passed************")
                    self.lp.clickTV()
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*********Failed************")
                    # self.lp.clickTV()
                    # self.lp.clickLogout();
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*********Failed************")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("*********Passed************")
                    lst_status.append("Pass")
            print(lst_status)

        if "Pass" in lst_status:
            assert True
            self.logger.info("*****Testcase_002 Multilogin is passed****")
            self.driver.close()

        else:
            self.logger.error("*****Testcase_002 Multilogin is Failed****")
            self.driver.close()
            assert False

        self.logger.info("*****End of Multilogin Testcase_002 *******")
        self.logger.info("*****Testcase_002 is completed*******")
