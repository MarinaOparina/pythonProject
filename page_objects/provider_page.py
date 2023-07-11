from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ProviderPage(BasePage):
    __url = "https://finance.yahoo.com/quote/DB1.DE?fr=sycsrp_catchall"
    __price_locator = "//*[@data-symbol='DB1.DE' and @data-test='qsp-price']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        self._driver.get(self.__url)
        self._driver.find_element(By.NAME, "reject").click()

    def get_price(self):
        provider_price = self._driver.find_element(By.XPATH, self.__price_locator).text
        print("UI price_yahoo " + provider_price + " ")
        return provider_price
