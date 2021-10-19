from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_cart_items(self):
        assert self.is_not_element_present(*BasePageLocators.CART_ITEM), "Cart items are presented, but should not be"

    def should_be_empty_cart_message(self):
        assert self.is_element_present(
            *BasePageLocators.CART_EMPTY), "Empty cart message is not presented, but should be"
