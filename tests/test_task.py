import pytest

from page_objects.db_page import DBPage
from page_objects.provider_page import ProviderPage


class TestScenarios:

    @pytest.mark.compare
    def test_compare(self, driver):
        # Open deutsche boerse page
        db_page = DBPage(driver)
        db_page.open_db_page()

        # Get price
        price = db_page.get_price_db()
        print("Site price  =" + price + " ")

        # Open Provider page
        provider_page = ProviderPage(driver)
        provider_page.open_page()

        # Get price
        price_provider = provider_page.get_price()
        print("Price_provider =" + price_provider + " ")

        assert price == price_provider, "The prices are are different. Site price = " + price + " provider provider price = " + price_provider
