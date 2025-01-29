from playwright.sync_api import expect, Page

from playwright_python.pythonautomation.src.pages.LoginPage import LoginPage


def test_login_with_standard_user(set_up_and_tear_down):
    page = set_up_and_tear_down
    login_page = LoginPage(page)
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    products_page = login_page.do_login(credentials)
    expect(products_page.products_header).to_be_visible()
    expect(products_page.products_header).to_have_text("Products")


def test_login_with_invalid_user(set_up_and_tear_down):
    page = set_up_and_tear_down
    login_page = LoginPage(page)
    credentials = {"username": "invalid_user", "password": "secret_sauce"}
    products_page = login_page.do_login(credentials)

    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    expect(login_page.error_message).to_contain_text(expected_error_message)


def test_login_with_no_credentials(set_up_and_tear_down):
    page = set_up_and_tear_down
    login_page = LoginPage(page)
    login_page.click_login()

    expected_error_message = "Epic sadface: Username is required"
    expect(login_page.error_message).to_contain_text(expected_error_message)


def test_access_inventory_without_login(set_up_and_tear_down):
    page = set_up_and_tear_down
    page.goto("https://www.saucedemo.com/inventory.html")
    expected_error_msg = "Epic sadface: You can only access '/inventory.html' when you are logged in."
    login_page = LoginPage(page)
    expect(login_page.error_message).to_contain_text(expected_error_msg)
