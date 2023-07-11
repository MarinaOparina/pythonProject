import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class DBPage(BasePage):
    __url = "https://deutsche-boerse.com/dbg-de/"
    __iframe_locator = "//*[contains(@class,'container') and child::h2[contains(text(),'Deutsche Börse AG')]]//iframe"
    __price_bd_locator = "closing_price"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_db_page(self):
        self._driver.get(self.__url)

    def get_price_db(self):
        iframe = self._driver.find_element(By.XPATH, self.__iframe_locator)
        self._driver.switch_to.frame(iframe)
        price_bd = self._driver.find_element(By.CLASS_NAME, "closing_price").text.replace(" €", "").replace(",", ".")
        return price_bd
