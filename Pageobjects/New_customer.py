import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import string
import random

class newly_added_customers:
    Dashboard_xpath = "//button[contains(text(),'Dashboard')]"
    Home_id = "Home"
    Customer_xpath = "//div[3]/div[2]/div/div/div"
    Add_new_customer_xpath = "//span[4]/img"
    Fullname_xpath = "//div[@id='CustomerModal']/div/div/div/div/div/input"
    Gender_name = "gender"
    Customer_Email_name = "styleemail"
    PhoneNumber_name = "stylephone"
    Customer_Add_button_xpath = "//button[contains(.,'ADD')]"


    def __init__(self,driver):
        self.driver=driver


    def clickdashboard(self):
        self.driver.find_element_by_xpath(self.Dashboard_xpath).click()

    def clickhome(self):
        self.driver.find_element_by_id(self.Home_id).click()

    def clickcustomer(self):
         self.driver.find_element_by_xpath(self.Customer_xpath).click()

    def clickAdd_new_customer(self):
        self.driver.find_element_by_xpath(self.Add_new_customer_xpath).click()

    def setFullname(self,fullname):
        self.driver.find_element_by_xpath(self.Fullname_xpath).send_keys(fullname)
        #fullname = (random.choice(string.ascii_letters.upper()) + random.choice(
            #string.ascii_letters.lower()) + random.choice(string.ascii_letters.lower()) + random.choice(
            #string.ascii_letters.lower()))
        #print(fullname)
        #self.setFullname.send_keys(fullname)


    def clickgender(self):
        self.driver.find_element_by_name(self.Gender_name).click()

    def setCustomeremail(self,email):
        self.driver.find_element_by_name(self.Customer_Email_name).send_keys(email)

    def setphonenumber(self,phonenumber):
        self.driver.find_element_by_name(self.PhoneNumber_name).send_keys(phonenumber)

    def clickcustomeraddbutton(self):
        self.driver.find_element_by_xpath(self.Customer_Add_button_xpath).click()








