from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import string
import random

from selenium.webdriver.remote.webelement import WebElement

driver: WebDriver = webdriver.Chrome(executable_path="C:\\Users\\HUBINO\\PycharmProjects\\Babria\\chromedriver.exe")
driver.maximize_window()
driver.get("http://dev-portal.barbria.com/")
print(driver.title)
username = driver.find_element_by_id("emailId")
password = driver.find_element_by_id("passView")
login_button = driver.find_element_by_xpath("//button[@name='SignIn']")
username.send_keys("naturals@mailinator.com")
password.send_keys("hubino@123")
login_button.click()


time.sleep(2)
# assert "salon" in driver.page_source


# Dashboard
time.sleep(5)
dashboard = driver.find_element_by_xpath("//button[contains(text(),'Dashboard')]")
dashboard.click()

time.sleep(3)

# Home
home = driver.find_element_by_id("Home")
home.click()

time.sleep(2)
# Customer
customer = driver.find_element_by_xpath("//div[3]/div[2]/div/div/div")
customer.click()

time.sleep(3)

# Customer + icon
Add_new_Customer = driver.find_element_by_xpath("//span[4]/img")
Add_new_Customer.click()

time.sleep(2)

# Customer Details
Fullname = driver.find_element_by_xpath("//div[@id='CustomerModal']/div/div/div/div/div/input")
name=(random.choice(string.ascii_letters.upper())+random.choice(string.ascii_letters.lower())+random.choice(string.ascii_letters.lower())+random.choice(string.ascii_letters.lower()))
print(name)
Fullname.send_keys(name)
Gender = driver.find_element_by_name("gender")
Gender.click()

# Gender_Male= driver.find_element_by_name("gender")

# Email
Customer_Email = driver.find_element_by_name("styleemail")
Customer_Email.send_keys("msd2@mailinator.com")

# phone_number
PhoneNumber = driver.find_element_by_name("stylephone")
lower_limit =8000000000 # Can be anything
upper_limit =9999999999 # Again, can be anything
number=(random.randint(lower_limit,upper_limit))
print(number)
PhoneNumber.send_keys(number)

# Customer_Add_button
Customer_Add_button = driver.find_element_by_xpath("//button[contains(.,'ADD')]")
Customer_Add_button.click()
#pop up message
time.sleep(3)

#pop_up=driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/button").text
pop_up=driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div").text
print(pop_up)

time.sleep(4)
Customer_search=driver.find_element_by_xpath("//div[@id='DashboardList']/div/div[2]/div[12]/p/div/div/div/div/div/div/div/div/span/input")
Customer_search.send_keys("Besil")

time.sleep(6)

#DashboardList=driver.find_element_by_id("DashboardList").text
#print(DashboardList)

customerdata=driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[12]").text
#//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[12]/div[1]
print(customerdata)


if 'Besil' in customerdata:
    assert True
else:
    assert False




