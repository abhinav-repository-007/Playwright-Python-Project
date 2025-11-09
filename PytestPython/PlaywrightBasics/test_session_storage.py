from playwright.sync_api import Playwright, expect

from PytestPython.Web_API.utils.apiBase import APIUtils


def test_session_storage(playwright:Playwright):
    #1. Generate the token
    api_utils = APIUtils()
    token_value = api_utils.getToken(playwright)

    #2. launch the browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #3. Enter a javascript script to inject in session local storage
    # All the javascript codes are written in triple quotes
    # Add f in start to mention constant str and var in same func
    page.add_init_script(f"""localStorage.setItem('token', '{token_value}')""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

    context.close()