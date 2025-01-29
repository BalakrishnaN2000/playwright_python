class ProductsPage:
    def __init__(self, page):
        self.page = page
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

    def get_add_or_remove_product_by_name_locator(self, product_name):
        return self.page.locator(f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item_label']/following-sibling::div//button")

    def click_add_to_cart_or_remove(self, product):
        self.get_add_or_remove_product_by_name_locator(product).click()
