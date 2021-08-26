"""
This module is where test cases are made for interactions on the main page.

Functions will start with test_ so they are detected by pytest. Test cases typically check one of the following or more:
    - UI updates
    - Images load
    - Audio plays
    - Text is accurate
    - Backend updates
    - Links are correct
"""

import pdb  # Use pdb.set_trace() to check the contents of the web element during test case creation
import time

import pytest
from selenium import webdriver
import page


class TestHome:

    @pytest.fixture  # This allows the test cases to find and run the function as a setup and teardown
    def setup_driver(self) -> None:
        """Function used for setting up the case with a fresh site load and for tearing down between cases."""
        self.driver = webdriver.Chrome(r"C:\Testing\chromedriver.exe")
        self.driver.get("http://demostore.supersqa.com/")
        yield  # This allows the test functions to complete and ends with teardown.
        self.driver.close()

    def test_title(self, setup_driver):  # The setup_driver argument is used so that it acts as a test case wrapper
        """Basic case to make sure the site loads without going to the wrong page or other errors"""
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match()  # Simple check to make sure there is no major error before testing starts

    def test_main_elements_loaded(self, setup_driver):
        """Test case to check elements loaded on the main page"""
        main_page = page.MainPage(self.driver)
        assert main_page.does_site_header_match("DemoStore\nJust another WordPress site")
        assert main_page.does_navbar_match("Home\nCart\nCheckout\nMy account\nSample Page")

    def test_search_hoodie(self, setup_driver):
        """Test case is for checking the search function on the main page works"""
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match()  # Checks the main page when no title is passed through
        main_page.enter_search_field("Hoodie")
        assert main_page.does_title_match(r"Search Results for “Hoodie” – DemoStore")  # Checking the right page loaded
        search_page = page.SearchPage(self.driver)
        assert search_page.read_search_result("Hoodie")
        search_page.check_for_product("Hoodie")

    def test_check_cart(self, setup_driver):
        """Test Case is for making sure the hoodie is added to the cart and all site behaviors update as expected"""
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match()  # Default check is for the main mage.
        main_page.add_hoodie_to_cart()
        main_page.check_cart_total("$33.41 1 item")  # Checking the total and the quantity as a string
        time.sleep(1)  # Giving 1 second, woocommerce will not load the item in the cart if moving too fast
        main_page.click_cart_button()
        assert main_page.does_title_match(r"Cart – DemoStore")  # Confirming the right page loaded
        cart_page = page.CartPage(self.driver)
        assert cart_page.check_for_product("Hoodie")  # Checking that the item added on the main page is following

    def test_hoodie_and_beanie(self, setup_driver):
        """
        Test case is for selecting the hoodie and beanie from the main page
            - make sure the cart button has the items added to the total
            Updates:
            - make sure the hovering over the cart button shows the items
            - make sure the cart page has both elements and the same total as the main page
        """
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match()  # Make sure we are on the main page.
        main_page.add_beanie_to_cart()
        main_page.check_cart_total("$16.27 1 item")
        main_page.add_hoodie_to_cart()
        main_page.check_cart_total("$49.68 2 items")


if __name__ == "__main__":
    pytest.main()
