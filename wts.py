'''import pywhatkit
pywhatkit.sendwhatmsg('+91 7904346865','Hi', 11, 58)'''

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

#s = Service("E:\\PycharmProjects\\Babria\\chromedriver.exe")
#driver = webdriver.Chrome(service=s)
#driver=webdriver.Chrome(executable_path="E:\\PycharmProjects\\Babria\\chromedriver.exe")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://seithi.mediacorp.sg/profile/register?redirect_url=/homepage&bookmark")
wait_time_N = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "edit-password")))
log_scroll_sign_up_N = driver.find_element(By.ID, "edit-password")
driver.execute_script("arguments[0].scrollIntoView();", log_scroll_sign_up_N)
time.sleep(3)
#gender =WebDriverWait(driver,2).until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//*[@id='me-connect-register']/div/div/div[7]/div/div/span/span[1]/span/span[2]"))).click()

#new=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='select2-edit-gender-result-ksjc-female']")))

#gender=driver.find_element(By.XPATH,"//*[@id='me-connect-register']/div/div/div[7]/div/div/span/span[1]/span")
gender=driver.find_element(By.ID,"select2-edit-gender-container")
gender.click()
time.sleep(5)
gen_1=driver.find_element(By.ID,"select2-edit-gender-result-1d1q-male")
gen_1.click()
time.sleep(2)
Date_of_birth = driver.find_element(By.ID, "edit-dob")
Date_of_birth.clear()
Date_of_birth.send_keys("1994-07-09")
Date_of_birth.clear()
Date_of_birth.send_keys("07-07-1984")
Check_box = driver.find_element(By.ID, "edit-terms-condition")
Check_box.click()
time.sleep(6)
Create_now = driver.find_element(By.XPATH, "//*[@id='me-connect-register']/div/div/button")
Create_now.click()
time.sleep(4)

