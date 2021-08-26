import pdb

from locator import *
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver
        super().__init__()


class MainPage(BasePage):

    def is_title_matches(self, to_match="DemoStore – Just another WordPress site"):
        return to_match in self.driver.title

    def enter_search_field(self, sending):
        element = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        element.clear()
        element.send_keys(sending)
        element.send_keys(Keys.ENTER)

    def read_search_result(self, expected_result):
        element = self.driver.find_element(*SearchResultLocators.SEARCH_RESULT)
        return expected_result in element.text

    def check_for_product(self, expected_result):
        element = self.driver.find_element(*SearchResultLocators.PRODUCT_RESULT)
        return expected_result in element.text

    def click_cart_button(self):
        element = self.driver.find_element(*MainPageLocators.CART_BUTTON)
        element.click()
