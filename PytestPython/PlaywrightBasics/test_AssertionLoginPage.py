from playwright.sync_api import Page
from playwright.sync_api import expect


def test_loginPage(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()        #Assertion
    # Now no need of wait, as we have used assertion.
