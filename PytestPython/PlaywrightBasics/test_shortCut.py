from playwright.async_api import Page
# When only 1 browser, 1 page, in headless = True mode,needs to be invoked.

# page = fixture     Page = Class       playwright.sync_api = package > coming from pytest-playwright plugin.
def test_shortCut(page : Page):
    page.goto("http://www.rahulshettyacademy.com/")
