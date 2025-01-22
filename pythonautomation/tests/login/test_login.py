from playwright.sync_api import expect, Page


def test_login_with_standard_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator(".title")
    expect(products_header).to_have_text("Products")


def test_login_with_invalid_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("invalid_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    error_message = page.locator("h3[data-test='error']")
    expect(error_message).to_contain_text(expected_error_message)


def test_login_with_no_credentials(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#login-button").click()

    expected_error_message = "Epic sadface: Username is required"
    error_message = page.locator("h3[data-test='error']")
    expect(error_message).to_contain_text(expected_error_message)
