from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import time
import string
import random

s=Service("E:\\PycharmProjects\\Babria\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://seithi.mediacorp.sg/mediacorp-digital-network")
"""print(driver.title)
#Sign Up
driver.execute_script("window.scroll(0, 0);")
time.sleep(2)
user1=driver.find_element(By.XPATH,"//*[@id='profile-menu-nav']/ul/li[1]/a/span")
user1.click()
wait_time_3= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='me-connect-login']/div/div/div[7]/div/a[3]")))
log_scroll_sign_up=driver.find_element(By.XPATH,"//*[@id='me-connect-login']/div/div/div[7]/div/a[3]")
driver.execute_script("arguments[0].scrollIntoView();",log_scroll_sign_up)
time.sleep(3)
Sign_up=driver.find_element(By.XPATH,"//*[@id='edit-signup-button']")
Sign_up.click()
time.sleep(2)
First_name=driver.find_element(By.ID,"edit-first-name")
Last_name=driver.find_element(By.ID,"edit-last-name")
Email=driver.find_element(By.ID,"edit-email")
Password=driver.find_element(By.ID,"edit-password")
Confirm_password=driver.find_element(By.ID,"edit-confirm-password")
time.sleep(3)
#Sign_up_data
First_name.clear()
First_name.send_keys("John")
Last_name.clear()
Last_name.send_keys("Wick")
Email.clear()
Email_1=(random.choice(string.ascii_letters.upper())+random.choice(string.ascii_letters.lower())+random.choice(string.ascii_letters.lower())+random.choice(string.ascii_letters.lower()))
print("New user email:",Email_1+"@gmail.com")
Email.send_keys(Email_1+"@gmail.com")
Password.clear()
Password.send_keys("Dream@12345")
Confirm_password.clear()
Confirm_password.send_keys("Dream@12345")
wait_time_N= WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.ID,"edit-password")))
log_scroll_sign_up_N=driver.find_element(By.ID,"edit-password")
driver.execute_script("arguments[0].scrollIntoView();",log_scroll_sign_up_N)
time.sleep(4)
Gender=driver.find_element(By.XPATH,"//*[@id='me-connect-register']/div/div/div[7]/div/div/span/span[1]/span/span[2]").click()
time.sleep(2)
Male=driver.find_element(By.XPATH,"/html/body/span/span/span[2]/ul/li[2]").click()
Date_of_birth=driver.find_element(By.ID,"edit-dob")
Date_of_birth.clear()
Date_of_birth.send_keys("1994-07-09")
Date_of_birth.clear()
Date_of_birth.send_keys("07-07-1984")
Check_box=driver.find_element(By.ID,"edit-terms-condition")
Check_box.click()
time.sleep(3)
Create_now=driver.find_element(By.XPATH,"//*[@id='me-connect-register']/div/div/button")
Create_now.click()
time.sleep(8)
print(driver.title)
#Bookmark
Singapore_B=driver.find_element(By.XPATH,"//*[@id='main-nav']/ul/li[3]/a")
Singapore_B.click()
wait_time_B= WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='block-mc-seithi-theme-mainpagecontent']/article/div/div[2]/div[1]/section/div/div/div/div[1]/div[1]/div[1]/a/picture/img")))
Bookmark_data=driver.find_element(By.XPATH,"//*[@id='block-mc-seithi-theme-mainpagecontent']/article/div/div[2]/div[1]/section/div/div/div/div[1]/div[1]/div[1]/a/picture/img")#"//*[@id='block-mc-seithi-theme-mainpagecontent']/article/div/div[2]/div[1]/section/div/div/div/div[1]/div[1]/div[1]/a/picture/img")
driver.execute_script("arguments[0].scrollIntoView();",Bookmark_data)
Data_for_bm=driver.find_element(By.XPATH,"//*[@id='block-mc-seithi-theme-mainpagecontent']/article/div/div[2]/div[1]/section/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]")
Data_for_bm.click()
time.sleep(3)
#Bookmark=driver.find_element(By.XPATH,"//*[@id='tooltip-2031b359-d4bd-4787-9540-a8a4e4cca841']/div/div/div/a[1]/svg/use")
Bookmark=driver.find_element(By.LINK_TEXT,"விருப்பக்குறி")
Bookmark.click()
time.sleep(4)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.execute_script("window.scroll(0, 0);")
time.sleep(2)
user2=driver.find_element(By.XPATH,"//*[@id='profile-menu-nav']/ul/li[2]/a/span")
user2.click()
#user1.click()
wait_time_1= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT,"Bookmarks")))
Acc=driver.find_element(By.LINK_TEXT,"Bookmarks").click()
time.sleep(4)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.execute_script("window.scroll(0, 0);")
wait_time_C= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT,"கணக்கு")))
Bookmark_Acct=driver.find_element(By.LINK_TEXT,"கணக்கு")
driver.execute_script("arguments[0].scrollIntoView();",Bookmark_Acct)
Account_n=driver.find_element(By.LINK_TEXT,"கணக்கு").click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)"""
driver.execute_script("window.scroll(0, 0);")
time.sleep(4)
search=driver.find_element(By.XPATH,"//nav[@id='profile-menu-nav']/ul/li[4]/span/span").click()
time.sleep(2)
search_data=driver.find_element(By.ID,"algolia-search-input")
search_data.send_keys("season")
search_data.send_keys(Keys.RETURN)
time.sleep(5)
print(driver.title)
time.sleep(5)
driver.quit()

