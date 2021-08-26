"""
Module used for defining page functions.

Page functions are the interaction done on the page using the locators on the site and performing interactions such
as typing and clicking on links.

These will also return booleans meant to be read as a PASS or FAIL
"""
import pdb

from locator import *
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver
        super().__init__()


class MainPage(BasePage):

    def does_title_match(self, to_match="DemoStore – Just another WordPress site"):
        return to_match in self.driver.title

    def enter_search_field(self, sending):
        element = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        element.clear()
        element.send_keys(sending)
        element.send_keys(Keys.ENTER)

    def add_hoodie_to_cart(self):
        element = self.driver.find_element(*MainPageLocators.HOODIE_ADD_TO_CART)
        element.click()

    def add_beanie_to_cart(self):
        element = self.driver.find_element()

    def click_cart_button(self):
        element = self.driver.find_element(*MainPageLocators.CART_BUTTON)
        element.click()

    def check_cart_total(self, expected_total):
        element = self.driver.find_element(*MainPageLocators.CART_BUTTON)
        return expected_total in element.text


class SearchPage(BasePage):

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
