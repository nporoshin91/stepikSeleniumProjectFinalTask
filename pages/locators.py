from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOODS_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    GOODS_PRICE = (By.CSS_SELECTOR, ".product_main > p:nth-child(2)")
    SUCCESS_MESSAGES = (By.XPATH, "//*/div[@class='alertinner ']//strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group")
    CART_ITEM = (By.ID, "basket_formset")
    CART_EMPTY = (By.XPATH, "//div[@id='content_inner']/p[contains(text(), 'Your basket is empty')]")
