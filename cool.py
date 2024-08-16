import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

#s=Service("E:\\PycharmProjects\\Babria\\chromedriver.exe")
#driver=webdriver.Chrome(service=s)
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://trends.google.com/trends")

key1 = driver.find_element(By.XPATH,'//*[@id="sidenav-menu-btn"]/div')
key1.click()
time.sleep(1)

key2 = driver.find_element(By.XPATH,'//*[@id="sidenav-list-group-trends"]/md-item[2]/md-item-content/a/i')
key2.click()

x =(driver.find_element(By.XPATH,"//*[@id='select_12']"))
x.click()

drp = Select(x)
drp.select_by_index(2)
# noinspection PyUnresolvedReferences








