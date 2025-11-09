from playwright.sync_api import Page

#Heirarchy :
#API calls generate from browser -> Api calls contact servers and returns responses to browser ->
# browser use the response to generate HTML

fake_payload_response = {"data": [], "message": "No Orders"}

# route is passed as arg coz it captures the event on url
def intercept_response(route):
    # fulfil means how should I fulfil the API calls, and it will fulfil by giving orders.
    # When browser receives response from server, that response we can change to fake.
    route.fulfill(
        json=fake_payload_response
    )


def test_network_responses(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    #1. We have to tell playwright to listen the Network call
    # route is property which will monitor the url and capture all info/event for that api like request, response,
    # status code,etc. And intercept_response is fun which will act on that event.
    # url = taken from Order page UI, * is for all the Orders
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("abhinav0007@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
