class ProductsPage:
    def __init__(self, page):
        self._products_header = page.locator(".title")

    @property
    def products_header(self):
        return self._products_header
