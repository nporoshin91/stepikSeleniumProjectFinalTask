import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_success_messages()
    goods_name = page.get_goods_name()
    goods_price = page.get_goods_price()
    success_messages = page.get_success_messages()  # тот самый список с трёмя "зелёными" сообщениями

    # переменная необходима для того, чтобы выйти из цикла поиска сразу после нахождения совпадения и сохранить рез-тат
    item_in_message = False

    # пробуем найти название товара среди "зелёных" сообщений
    for message in success_messages:
        if goods_name == message:
            item_in_message = True
            break
        else:
            item_in_message = False
    if not item_in_message:
        assert False, "Success message doesn't contain goods name"

    # пробуем найти цену товара среди "зелёных" сообщений
    for message in success_messages:
        if goods_price == message:
            item_in_message = True
            break
        else:
            item_in_message = False
    if not item_in_message:
        assert False, "Success message doesn't contain goods price"

    page.should_not_be_success_message()


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.click_on_add_to_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.click_on_add_to_basket_button()
    page.should_be_disappered_success_message()


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
