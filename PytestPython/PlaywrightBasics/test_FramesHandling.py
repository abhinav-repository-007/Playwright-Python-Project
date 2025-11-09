from playwright.sync_api import Page, expect


def test_frames_handling(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #Frame
    #Below line will search frames in the page and return the object of that frame to a var.
    pageFrame = page.frame_locator("#courses-iframe") #id = courses-iframe
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")