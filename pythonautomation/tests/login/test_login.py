from playwright.sync_api import expect, Page

from playwright_python.pythonautomation.src.pages.LoginPage import LoginPage


def test_login_with_standard_user(set_up_and_tear_down):
    page = set_up_and_tear_down
    login_page = LoginPage(page)
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    products_page = login_page.do_login(credentials)
    expect(products_page.products_header).to_be_visible()
    expect(products_page.products_header).to_have_text("Products")


def xtest_login_with_invalid_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("invalid_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    error_message = page.locator("h3[data-test='error']")
    expect(error_message).to_contain_text(expected_error_message)


def xtest_login_with_no_credentials(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#login-button").click()

    expected_error_message = "Epic sadface: Username is required"
    error_message = page.locator("h3[data-test='error']")
    expect(error_message).to_contain_text(expected_error_message)
