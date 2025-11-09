from playwright.sync_api import Playwright

#Take payload in a var to look code simple
orderPayloadValue = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}

# All the API related methods will be defined under APIUtils class
class APIUtils:

    def getToken(self, playwright:Playwright, user_credentials):
        api_context = playwright.request.new_context(base_url= "https://rahulshettyacademy.com/")
        # We need to remove hard-coded email-password from there as well.
        # Hence pass the fixture user_credentials here as well as arg.
        user_email = user_credentials["userEmail"] #Take value in a var and pass in data
        user_password = user_credentials["userPassword"]
        response = api_context.post("api/ecom/auth/login",
                         data= {"userEmail": user_email , "userPassword": user_password})

        #To check login successful
        assert response.ok #will return True if response is OK

        print(response.json()) #We need to response in json to get token
        response_body = response.json()
        return response_body["token"]

    # Take user_credentials as 3rd arg to access email-password
    def createOrders(self, playwright:Playwright, user_credentials):

        token = self.getToken(playwright, user_credentials)

        # playwright.request property will help to make API calls, just like chromium helps to launch browser
        # In new_context(), we have to connect to a server via base url then we can use APIs
        api_context = playwright.request.new_context(base_url= "https://rahulshettyacademy.com/")
        response = api_context.post("api/ecom/order/create-order",
                         data= orderPayloadValue,
                         #Header accepts key-value pair
                         # For token to generate, we must login 1st.
                         headers=  {'Authorization' : token, # We need to pass token to verify the User for which order is placed.
                                    'Content-type' : 'application/json'} # To get the response in Json.
                                    )


        #Print to response to see in log
        print(response.json()) #Return response in json body, coz we need to catch Order Id from the Response body.
        order_id = response.json()
        return order_id["orders"][0]
