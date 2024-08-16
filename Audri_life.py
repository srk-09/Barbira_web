from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
s=Service("D:\\PycharmProjects\\Babria\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://dev-portal.audri.life/")
print(driver.title)
username=driver.find_element_by_id("input-one")
password=driver.find_element_by_id("input-two")
login_button=driver.find_element_by_id("input-three")
username.send_keys("audri-life@mailinator.com")
password.send_keys("Hubino@123")
login_button.click()
time.sleep(2)
Mail_url=driver.get("https://www.mailinator.com/v4/public/inboxes.jsp")
time.sleep(2)
Mail_email=driver.find_element_by_id("inbox_field")
Mail_email.send_keys("audri-life@mailinator.com")
Mail_email_Go=driver.find_element_by_xpath("//div[5]/button")
Mail_email_Go.click()
time.sleep(2)
Mail_Inbox=driver.find_element_by_xpath("//div[4]/div/div/table/tbody/tr/td[2]")
Mail_Inbox.click()
time.sleep(2)
Rambo= Mail_Inbox.text






