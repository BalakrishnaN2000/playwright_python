from playwright.sync_api import expect

from playwright_python.pythonautomation.src.pages.LoginPage import LoginPage


def test_add_product_to_cart(set_up_and_tear_down):
    page = set_up_and_tear_down
    login_page = LoginPage(page)
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    products_page = login_page.do_login(credentials)

    product_name = "Sauce Labs Backpack"
    products_page.click_add_to_cart_or_remove(product_name)
    expect(products_page.get_add_or_remove_product_by_name_locator(product_name)).to_have_text("Remove")


def test_remove_product_to_cart(set_up_and_tear_down):
    page = set_up_and_tear_down
    login_page = LoginPage(page)
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    products_page = login_page.do_login(credentials)

    product_name = "Sauce Labs Backpack"
    products_page.click_add_to_cart_or_remove(product_name)
    products_page.click_add_to_cart_or_remove(product_name)
    expect(products_page.get_add_or_remove_product_by_name_locator(product_name)).to_have_text("Add to cart")
