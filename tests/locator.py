from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CART_BUTTON = (By.ID, "site-header-cart")
    SEARCH_FIELD = (By.ID, "woocommerce-product-search-field-0")


class SearchResultLocators(object):
    SEARCH_RESULT = (By.CSS_SELECTOR, "#main > header > h1")
