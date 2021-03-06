from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

    def should_be_success_messages(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is presented," \
                                                                                   " but should not be"

    def should_be_disappered_success_message(self):
        assert self.is_disappeard(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is presented," \
                                                                          " but should not be"

    def get_goods_name(self):
        goods_name = self.browser.find_element(*ProductPageLocators.GOODS_NAME).text
        return goods_name

    def get_goods_price(self):
        goods_price = self.browser.find_element(*ProductPageLocators.GOODS_PRICE).text
        return goods_price

    def get_success_messages(self):
        # находим одним махом три WebElement'а на странице, каждый из которых это "зелёное" сообщение на странице
        elements = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)

        # достаём из каждого WebElement'а текст и добавляем его в список
        success_messages = [element.text for element in elements]
        return success_messages
