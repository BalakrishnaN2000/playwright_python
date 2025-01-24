from playwright.sync_api import Page, expect


def xtest_logout(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products_header = page.locator(".title")
    expect(products_header).to_have_text("Products")

    burger_menu_btn = page.locator("button[id*='burger-menu-btn']")
    burger_menu_btn.click()
    logout = page.locator("//a[text()='Logout']")
    logout.click()

    expect(page.locator("#login-button")).to_be_visible()
