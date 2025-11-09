from playwright.sync_api import Page
def test_childWindowhandle(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # Child page : page.expect.pop-up acts like listner for every step, if any new window comes
    with page.expect_popup() as newWindow:  # This is lika a closure for parent page.
        # This will hit the link n return obj for new page to the listner and save in newWindow
        page.locator(".blinkingText").filter(has_text="Free Access").click()

        # newWindow.value will return object of the new page.
        newPage = newWindow.value

        # text_content() = To get the whole content
        redText = newPage.locator(".red").filter(has_text="Please email").text_content()

        # "Please email us at mentor@rahulshettyacademy.com with below template to receive response"
        print(redText)

        # Split the line into 2 with 'at', 0 = Please email us, 1 = mentor@rahulshettyacademy.com with below template to receive response
        words = redText.split("at")

        # Again split with " ", hence email will extract from redText. Strip to trim leading n trailing spaces
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"    # Pytest Assertion


