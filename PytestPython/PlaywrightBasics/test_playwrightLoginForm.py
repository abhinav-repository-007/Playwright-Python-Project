from playwright.sync_api import Page
import time

def test_loginPage(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    # CSS Selector, uses locator when get_by_role / label does not work.
    page.locator("#terms").check()        # We have id = "terms", hence write "#terms". If we had class / tagname , then ".classValue", or tagname <>
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()       # Take value = "Sign In"
    time.sleep(5)
