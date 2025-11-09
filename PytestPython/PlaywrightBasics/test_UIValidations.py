import time

from playwright.sync_api import Page, expect


def test_ApplicationAutomation(page : Page):
    # Login
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")   #value
    page.get_by_role("link", name = "terms and conditions").click()
    page.locator("#terms").check()              # Scope is the whole page
    page.get_by_role("button", name = "Sign In").click()
    # Select Products (iphone X ,  and add to cart
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")    # locator(tagname).filter() => limits the scope
    iphoneProduct.locator("button").click()         # Limits the scope in card only.
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.locator("button").click()
    page.get_by_text("Checkout ").click()
    expect(page.locator(".media-body")).to_have_count(2)    # Assertion to check 2 items added to the cart
    # Assertion to check correct items added to cart
    #expect(page.locator(".media-body")).to_have_text("iphone X") #Dont use to_have_text() when locator is returning more than 1 element
    expect(page.locator(".media-body").filter(has_text="iphone X")).to_be_visible()
    expect(page.locator(".media-body").filter(has_text="Nokia Edge")).to_be_visible()
    # Assertion to check whether the products are in stock or not
    expect(page.locator(".text-success").filter(has_text="In Stock")).to_have_count(2)
    time.sleep(3)