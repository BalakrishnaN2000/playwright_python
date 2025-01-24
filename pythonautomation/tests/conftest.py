import pytest


@pytest.fixture()
def set_up_and_tear_down(page):
    page.set_viewport_size({"width": 1300, "height": 650})
    page.goto("https://www.saucedemo.com/")
    yield page
