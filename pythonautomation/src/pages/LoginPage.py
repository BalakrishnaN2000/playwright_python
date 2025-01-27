from playwright_python.pythonautomation.src.pages.ProductsPage import ProductsPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.locator("#user-name")
        self._password = page.locator("#password")
        self._login_btn = page.locator("#login-button")
        self._error_message = page.locator("h3[data-test='error']")

    def enter_username(self, username):
        self._username.fill(username)

    def enter_password(self, password):
        self._password.fill(password)

    @property
    def login_button(self):
        return self._login_btn

    def click_login(self):
        self.login_button.click()

    def do_login(self, credentials):
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_login()
        return ProductsPage(self.page)

    @property
    def error_message(self):
        return self._error_message
