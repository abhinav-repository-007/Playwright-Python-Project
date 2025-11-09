from playwright.sync_api import Playwright, expect

from PytestPython.Web_API.utils.apiBase import APIUtils


# Login, placing order and taking Order Id thru UI
# Checking Order ID matching with API response thru API

def test_e2e_web_api(playwright : Playwright):
    # we cant use page as we have to do api calls as well, hence playwright
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 1. Create Order via API n get the Order ID
    # Create 1 dir 'utils' in Web_API, and make py file 'apiBase.py'.
    # Now call the class and its method to create Order
    api_utils = APIUtils()
    orderId = api_utils.createOrders(playwright) #Use same instance as playwright which we already created before for
    # test_e2e_web_api(), Hence 1 instance per test should be created and used throughout the test.

    # 2. Login into app via UI
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("abhinav0007@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    #3. Go to Orders page, n check order is present in UI
    # We have already placed order from API, hence directly goto Order page
    page.get_by_role("button", name="ORDERS").click()
    # locate for all rows, then search for the row having our OrderId
    desired_row = page.locator("tr").filter(has_text= orderId)
    desired_row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close() #Optional
