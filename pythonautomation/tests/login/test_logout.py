from playwright.sync_api import Page, expect

from playwright_python.pythonautomation.src.pages.LoginPage import LoginPage


def test_logout(set_up_and_tear_down):
    # page.goto("https://www.saucedemo.com/")
    # page.locator("#user-name").fill("standard_user")
    # page.locator("#password").fill("secret_sauce")
    # page.locator("#login-button").click()
    page = set_up_and_tear_down
    login_page = LoginPage(page)
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    products_page = login_page.do_login(credentials)

    expect(products_page.products_header).to_have_text("Products")

    products_page.do_logout()

    expect(login_page.login_button).to_be_visible()
