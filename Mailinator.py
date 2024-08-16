from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path="D:\\PycharmProjects\\Babria\\chromedriver.exe")
driver.maximize_window()

Mail_url=driver.get("https://www.mailinator.com/v4/public/inboxes.jsp")
Mail_email=driver.find_element_by_id("inbox_field")
Mail_email.send_keys("audri-life@mailinator.com")
Mail_email_Go=driver.find_element_by_xpath("//div[5]/button")
Mail_email_Go.click()
time.sleep(2)
Mail_Inbox=driver.find_element_by_xpath("//div[4]/div/div/table/tbody/tr/td[2]")
Inbox=Mail_Inbox.text
print(Inbox)
Mail_Inbox.click()
time.sleep(2)
OTP1=driver.find_element_by_id("//p[contains(text(),'<#> 2438 is your One Time Verification (OTP) code ')]")
slow=OTP1.text
print(slow)
print(driver.current_url)

"""web_url = driver.get("http://beacon-stage.usvi.care/")
time.sleep(2)
Email = driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[3]/div[3]/input")
Email.send_keys("sivaramakrishnan.s@hubino.com")

submit = driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[3]/div[4]/button")
submit.click()
time.sleep(2)
Lab_dropdown = driver.find_element_by_xpath("//div[@id='root']/div/div[3]/div/div[3]/select")
Lab_dropdown.click()
time.sleep(2)
Lab_dropdown_select = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div[3]/select/option[2]")
Lab_dropdown_select.click()
Lab_submit = driver.find_element_by_xpath("//div[@id='root']/div/div[3]/div/div[4]/button")
Lab_submit.click()
time.sleep(5)
print("Title of the page",driver.title)
print("URL",driver.current_url)
Mail_url = driver.execute_script(
    "window.open('https://outlook.office.com/mail/inbox/id/AAQkADJmYWQ3ZGM5LTRmNzMtNGY5MC1iMTA2LWVjN2E5MGUxOTFmZgAQAMU1E6aHMXVGhWxDXqgWHco%3D')")
driver.switch_to.window(driver.window_handles[1])
#driver.switch_to_window(driver.window_handles[1])
time.sleep(5)
Email = driver.find_element_by_id("i0116")
Email.send_keys("sivaramakrishnan.s@hubino.com")
Next = driver.find_element_by_id("idSIButton9")
Next.click()
time.sleep(2)
Pass = driver.find_element_by_id("i0118")
Pass.send_keys("srk@4567")
sign = driver.find_element_by_id("idSIButton9")
time.sleep(2)
sign.click()
time.sleep(2)
no = driver.find_element_by_id("idBtn_Back")
no.click()
time.sleep(5)
Filter=driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div[3]/div")
Filter.click()
time.sleep(2)
Unread=driver.find_element_by_xpath("//li[2]/button/div/span")
Unread.click()
time.sleep(2)
Mail_click=driver.find_element_by_xpath("//span[contains(.,'Email OTP Verification')]")
Mail_click.click()
time.sleep(2)
Code = driver.find_element_by_xpath("//p[3]")
odd = Code.text
print("OTP= ",odd)
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
#driver.switch_to_window(driver.window_handles[0])
time.sleep(2)
Mail_otp = driver.find_element_by_xpath("//input")
Mail_otp.send_keys(odd)
time.sleep(2)
Otp_submit=driver.find_element_by_xpath("//button[contains(.,'Submit')]")
Otp_submit.click()"""
