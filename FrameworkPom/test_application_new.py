import json

import pytest
from playwright.sync_api import Playwright

from PageObjectClass.Login import LoginPage
from Utils.api_base import APIMethods

with open('Data/credentials.json') as f:
    file_data = json.load(f)
    print(file_data) #Will print file data
    user_creds_list = file_data['user_login']


@pytest.mark.parametrize('user_credentials', user_creds_list)
def test_pom_application(playwright : Playwright, browser_selection, user_credentials):

    #Create Order
    api_calls = APIMethods()
    order_id = api_calls.createOrders(playwright, user_credentials)

    user_email = user_credentials["userEmail"]
    user_password = user_credentials["userPassword"]

    # Replace page in LoginPage(page) with browser-selection, coz browser_selection fixture defined in conftest is returning page
        # object n saving browser_selection
    sign_in = LoginPage(browser_selection)
    sign_in.launch_url()
    dashboard = sign_in.login(user_email, user_password)
    order_details = dashboard.click_orders()
    order_history = order_details.click_view_for_order(order_id)
    order_history.verify_order()












