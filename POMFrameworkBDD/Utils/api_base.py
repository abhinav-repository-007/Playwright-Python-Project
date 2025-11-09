from playwright.sync_api import Playwright

order_payload_value = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}

class APIMethods:

    def getToken(self, playwright : Playwright, user_credentials):
        api_context = playwright.request.new_context(base_url= "https://rahulshettyacademy.com/")
        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]
        response = api_context.post("api/ecom/auth/login",
                         data= {"userEmail": user_email, "userPassword": user_password},
                        headers={"Content-Type": "application/json"}
                         )

        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def createOrders(self, playwright : Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_context = playwright.request.new_context(base_url = "https://rahulshettyacademy.com/")
        response = api_context.post("api/ecom/order/create-order",
                         data= order_payload_value,
                         headers= {
                             "Authorization": token,
                             "Content-Type": "application/json"}
                         )
        print(response.json())
        order_id = response.json()
        return order_id["orders"][0]

