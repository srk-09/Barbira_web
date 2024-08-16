from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
@pytest.fixture()
def setup():
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver=webdriver.Chrome()
        driver = webdriver.Chrome(options=options)
        return driver





##########HTML REPORT - Adding environment info#########
def pytest_configure(config):
    config._metadata['Project name'] = 'Barbria'
    config._metadata['Tester'] = 'Sivaramakrishnan.S'
    config._metadata['Module'] = 'Login Module with MultiLogin'
    config._metadata['Project Manager'] = 'Karthikeyan'


####Removing unwanted info########

@pytest.mark.skip()
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
