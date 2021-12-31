"""
Module used for defining page functions.

Page functions are the interaction done on the page using the locators on the site and performing interactions such
as typing and clicking on links.

These will also return booleans meant to be read as a PASS or FAIL
"""

import pdb  # Use pdb.set_trace() to check the contents of the web element during test case creation

from locator import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class BasePage(object):
    """Base class object for inheriting the web driver"""
    def __init__(self, driver) -> None:
        self.driver = driver
        super().__init__()


class MainPage(BasePage):
    """
    Class for functions to be used when testing the main page.

    Test Cases to write:
        - Hover over cart shows items
    """

    def does_title_match(self, to_match="DemoStore – Just another WordPress site"):
        return to_match in self.driver.title

    def does_site_header_match(self, to_match):
        element = self.driver.find_element(*MainPageLocators.SITE_HEADER)
        return to_match in element.text

    def does_navbar_match(self, to_match):
        element = self.driver.find_element(*MainPageLocators.NAV_MENU)
        return to_match in element.text

    def enter_search_field(self, sending):
        element = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        element.clear()
        element.send_keys(sending)
        element.send_keys(Keys.ENTER)

    def add_hoodie_to_cart(self):
        element = self.driver.find_element(*MainPageLocators.HOODIE_ADD_TO_CART)
        element.click()

    def add_beanie_to_cart(self):
        element = self.driver.find_element(*MainPageLocators.BEANIE_ADD_TO_CART)
        element.click()

    def click_cart_button(self):
        element = self.driver.find_element(*MainPageLocators.CART_BUTTON)
        element.click()

    def check_cart_total(self, expected_total):
        element = self.driver.find_element(*MainPageLocators.CART_BUTTON)
        return expected_total in element.text
    
    def sort_by_value(self, dropdown_value):
        element = self.driver.find_element(*MainPageLocators.SORT_DROPDOWN)
        dropdown = Select(element)
        dropdown.select_by_value(dropdown_value)
        return dropdown_value in self.driver.title
        

class SearchPage(BasePage):
    """
    Class for all functions on the search results screen

    Test Cases to write:
        - Check that an invalid search with no results works as expected
        - Check that items can be selected and interacted with
    """

    def read_search_result(self, expected_result):
        element = self.driver.find_element(*SearchResultLocators.SEARCH_RESULT)
        return expected_result in element.text

    def check_for_product(self, expected_result):
        element = self.driver.find_element(*SearchResultLocators.PRODUCT_RESULT)
        return expected_result in element.text


class CartPage(BasePage):
    """
    Functions to be ran while on the Cart screen

    Tests to make:
        - Check removing items
        - Check product costs add up to total
        - Check that the product thumbnail loads
        - Check that coupons work (and that entering random letters does not work)
    """

    def check_for_product(self, product_name):
        element = self.driver.find_element(*CartPageLocators.PRODUCT_NAME)
        return product_name in element.text

    def check_product_cost(self, product_cost):
        element = self.driver.find_element(*CartPageLocators.PRODUCT_PRICE)
        return product_cost in element.text
