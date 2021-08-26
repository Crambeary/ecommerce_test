import pdb
import time

import pytest
from selenium import webdriver
import page


class TestHome:

    @pytest.fixture  # This allows the test cases to find and run the function as a setup and teardown
    def setup_driver(self) -> None:
        self.driver = webdriver.Chrome(r"C:\Testing\chromedriver.exe")
        self.driver.get("http://demostore.supersqa.com/")
        yield  # This allows the test functions to complete and ends with teardown.
        self.driver.close()

    def test_title(self, setup_driver):
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match()  # Simple check to make sure there is no major error before testing starts

    def test_search_hoodie(self, setup_driver):
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match()  # Checks the main page when no title is passed through
        main_page.enter_search_field("Hoodie")
        assert main_page.does_title_match(r"Search Results for “Hoodie” – DemoStore")  # Checking the right page loaded
        search_page = page.SearchPage(self.driver)
        assert search_page.read_search_result("Hoodie")
        search_page.check_for_product("Hoodie")

    def test_check_cart(self, setup_driver):
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match()  # Default check is for the main mage.
        main_page.add_hoodie_to_cart()
        main_page.check_cart_total("$33.41 1 item")  # Checking the total and the quantity as a string
        time.sleep(1)  # Giving 1 second, woocommerce will not load the item in the cart if moving too fast
        main_page.click_cart_button()
        assert main_page.does_title_match(r"Cart – DemoStore")  # Confirming the right page loaded
        cart_page = page.CartPage(self.driver)
        assert cart_page.check_for_product("Hoodie")  # Checking that the item added on the main page is following


if __name__ == "__main__":
    pytest.main()
