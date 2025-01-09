import playwright.async_api
import asyncio


async def main():
    async with playwright.async_api.async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=False)
        page = await browser.new_page()
        await page.goto("https://www.saucedemo.com/")
        print(page.url)
        print(await page.title())
        # await page.screenshot(path="example.png")
        await browser.close()
        await p.stop()

if __name__ == "__main__":
    asyncio.run(main())
