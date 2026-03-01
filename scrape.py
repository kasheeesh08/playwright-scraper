import asyncio
from playwright.async_api import async_playwright

SEEDS = list(range(5, 15))
BASE_URL = "https://sanand0.github.io/tdsdata/js_table/?seed="

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        grand_total = 0

        for seed in SEEDS:
            page = await browser.new_page()
            await page.goto(f"{BASE_URL}{seed}", wait_until="networkidle")
            await page.wait_for_selector("table")

            cells = await page.query_selector_all("table td")
            for cell in cells:
                text = await cell.inner_text()
                try:
                    grand_total += int(text.strip())
                except:
                    pass

            await page.close()

        await browser.close()
        print("FINAL TOTAL:", grand_total)

asyncio.run(main())
