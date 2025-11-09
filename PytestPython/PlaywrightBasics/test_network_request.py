import time
from playwright.sync_api import Page


#API calls generate from browser -> Api calls contact servers and returns responses to browser
# Now we will mock the request done by API to Server, before request reaching to Server.

def intercept_request(route):
    #Continue the request call to Server with this new url
    route.continue_(url= "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69072074f669d6cb0a3c122f")


def test_network_request(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    #1. We have to tell playwright to listen the Network call
    # route is property which will monitor the url and capture all info/event for that api like request, response,
    # status code,etc. And intercept_request is func which will act on that event.
    # url = taken from Order page UI, * is for all the Orders
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("abhinav0007@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="View").first.click() #Will click on 1st View button
    # time.sleep(5)
    result_text = page.locator(".blink_me").text_content()
    print(result_text)
    assert result_text == "You are not authorize to view this order"