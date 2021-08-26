from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CART_BUTTON = (By.ID, "site-header-cart")
    SEARCH_FIELD = (By.ID, "woocommerce-product-search-field-0")
    HOODIE_ADD_TO_CART = (By.CSS_SELECTOR, "#main > ul > li.product.type-product.post-13.status-publish.instock"
                                           ".product_cat-hoodies.has-post-thumbnail.shipping-taxable.purchasable"
                                           ".product-type-simple > "
                                           "a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")


class SearchResultLocators(object):
    SEARCH_RESULT = (By.CSS_SELECTOR, "#main > header > h1")
    PRODUCT_RESULT = (By.CSS_SELECTOR, "#main > ul")


class CartPageLocators(object):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#post-7 > div > div > form > table > tbody > "
                                     "tr.woocommerce-cart-form__cart-item.cart_item > td.product-name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#post-7 > div > div > form > table > tbody > "
                                      "tr.woocommerce-cart-form__cart-item.cart_item > td.product-price")
