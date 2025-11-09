
# 'playwright' is a fixture, pre-defined in pytest-playwright package. Its a Global fixture
# def test_playwrightBasics(playwright):
#     # Invoke chromium engine for browser in headless = false mode, to see all function.
#     # By-default it invokes in headless = True, to make run faster
#     browser = playwright.chromium.launch(headless=False)
#
#     # Open browser in-cognito mode
#     context = browser.new_context()
#
#     # Open a new page
#     page = context.new_page()
#
#     # Launch website
#     page.goto("https://www.rahulshettyacademy.com")

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.rahulshettyacademy.com/")




