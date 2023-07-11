import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome()
    #my_driver = webdriver.Firefox()

    my_driver.maximize_window()
    my_driver.implicitly_wait(10)
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()
