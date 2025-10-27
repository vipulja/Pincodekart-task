import pytest
from playwright.sync_api import sync_playwright

def test_add_item_to_cart():
    # Start Playwright and launch a headed (UI) browser
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False,slow_mo=2000)
    page = browser.new_page()

    try:
        # 1. Navigate to login page
        page.goto("https://www.saucedemo.com")
        # 2. Log in with provided credentials
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        # Wait until the inventory page loads by checking for the backpack's Add button
        page.wait_for_selector("#add-to-cart-sauce-labs-backpack")
        # 3. Identify and add "Sauce Labs Backpack" to the cart
        page.click("#add-to-cart-sauce-labs-backpack")
        # 4. Go to the shopping cart page
        page.click(".shopping_cart_link")
        # Wait for the cart page to load by checking for the item name element
        page.wait_for_selector(".inventory_item_name")
        # 5. Verify cart contents: item name and price
        item_name = page.inner_text(".inventory_item_name")
        item_price = page.inner_text(".inventory_item_price")
        assert item_name == "Sauce Labs Backpack", f"Expected item name to be 'Sauce Labs Backpack' got '{item_name}'"
        assert item_price == "$29.99", f"Expected price to be '$29.99' got '{item_price}'"
    finally:
        # Ensure browser is closed regardless of test outcome
        browser.close()
        pw.stop()
