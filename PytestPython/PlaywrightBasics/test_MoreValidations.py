import time

from playwright.sync_api import Page, expect


def test_moreValidations(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # Placeholder
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # Dialog Box
    page.on("dialog", lambda dialog: dialog.accept()) # lambda is 1 liner anonymous fun. The fun which does not have any name, arg, etc.
                                    # page.on(event, fun) => Act as listner for the page, whenever dialog box appears, it gonna accept it.
    page.get_by_role("button", name="Confirm").click()
    time.sleep(3)
