from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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
        if goods_name in message:
            item_in_message = True
            break
        else:
            item_in_message = False
    if not item_in_message:
        assert False, "Success message doesn't contain goods name"

    # пробуем найти цену товара среди "зелёных" сообщений
    for message in success_messages:
        if goods_price in message:
            item_in_message = True
            break
        else:
            item_in_message = False
    if not item_in_message:
        assert False, "Success message doesn't contain goods price"
