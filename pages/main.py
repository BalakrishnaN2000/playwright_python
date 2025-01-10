import playwright.async_api
import asyncio
from __init__ import *


async def main(browser_name, base_url, headless_mode):
    async with playwright.async_api.async_playwright() as p:
        print("browser_type = ", type(browser_name))
        print("url_type = ", type(base_url))
        print("headless_type = ", type(headless_mode))
        browser_name = await p.chromium.launch(channel=browser_name, headless=headless_mode)
        page = await browser_name.new_page()
        await page.goto(base_url)
        print(page.url)
        print(await page.title())
        # await page.screenshot(path="example.png")
        await browser_name.close()
        await p.stop()

asyncio.run(main(browser, url, headless))
