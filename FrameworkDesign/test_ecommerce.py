import json

import pytest
from playwright.sync_api import Playwright
from PytestPython.Web_API.utils.apiBase import APIUtils

# Open the Json file -> load json data into a var
with open('FrameworkDesign/Data/credentials.json') as f:
    file_data = json.load(f)
    print(file_data) #Will print file data
    user_creds_list = file_data['user_login'] #return list of dictionary

#user_creds will iterate in user_creds_list (we have 2 items in list)
@pytest.mark.parametrize('user_credentials', user_creds_list)
def test_ecommerce_framework(playwright : Playwright, user_credentials): #Fixtures should be mentioned in test
                                                                            # to be executed 1st
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIUtils()
    orderId = api_utils.createOrders(playwright, user_credentials)

    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill(user_credentials["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
    page.get_by_role("button", name="Login").click()