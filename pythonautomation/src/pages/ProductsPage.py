class ProductsPage:
    def __init__(self, page):
        self._products_header = page.locator(".title")
        self._burger_menu_btn = page.locator("button[id*='burger-menu-btn']")
        self._logout = page.locator("//a[text()='Logout']")

    @property
    def products_header(self):
        return self._products_header

    def click_burger_menu_btn(self):
        self._burger_menu_btn.click()

    def click_logout(self):
        self._logout.click()

    def do_logout(self):
        self.click_burger_menu_btn()
        self.click_logout()
