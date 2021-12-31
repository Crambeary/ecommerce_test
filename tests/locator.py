from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """Class that holds the locations of elements for the Main page"""
    SITE_HEADER = (By.CSS_SELECTOR, "#masthead > div.col-full > div.site-branding")
    NAV_MENU = (By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul")
    CART_BUTTON = (By.ID, "site-header-cart")
    SEARCH_FIELD = (By.ID, "woocommerce-product-search-field-0")
    HOODIE_ADD_TO_CART = (By.CSS_SELECTOR, "#main > ul > li.product.type-product.post-13.status-publish.instock"
                                           ".product_cat-hoodies.has-post-thumbnail.shipping-taxable.purchasable"
                                           ".product-type-simple > "
                                           "a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
    BEANIE_ADD_TO_CART = (By.CSS_SELECTOR, "#main > ul > li.product.type-product.post-15.status-publish.instock"
                                           ".product_cat-accessories.has-post-thumbnail.sale.shipping-taxable"
                                           ".purchasable.product-type-simple > "
                                           "a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#main > div:nth-child(2) > form > select")
    PRODUCT_RESULT = (By.CSS_SELECTOR,"#main > ul")
    ALBUM_PRODUCT = (By.CSS_SELECTOR, "#main > ul > li.product.type-product.post-23.status-publish.first"
                                      ".instock.product_cat-music.has-post-thumbnail.sale.downloadable"
                                      ".virtual.purchasable.product-type-simple")
    POPULARITY_DROPDOWN = (By.CSS_SELECTOR, "#main > div:nth-child(2) > form > select > option:nth-child(2)")

class SearchResultLocators(object):
    """Class that holds the locations of elements for the Search Results page"""
    SEARCH_RESULT = (By.CSS_SELECTOR, "#main > header > h1")
    PRODUCT_RESULT = (By.CSS_SELECTOR, "#main > ul")


class CartPageLocators(object):
    """Class that holds the locations of elements for the cart page"""
    PRODUCT_NAME = (By.CSS_SELECTOR, "#post-7 > div > div > form > table > tbody > "
                                     "tr.woocommerce-cart-form__cart-item.cart_item > td.product-name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#post-7 > div > div > form > table > tbody > "
                                      "tr.woocommerce-cart-form__cart-item.cart_item > td.product-price")
