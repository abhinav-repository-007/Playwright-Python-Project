from playwright.sync_api import Playwright

def test_firefoxLoginPage(playwright : Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    # context = firefoxBrowser.new_context()        #Can be skipped if we want only 1 window
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    