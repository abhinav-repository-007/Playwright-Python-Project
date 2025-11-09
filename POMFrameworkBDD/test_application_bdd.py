import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from PageObjectClass.Login import LoginPage
from Utils.api_base import APIMethods

#We have to tell which scenario it is associated to.
scenarios('Features/orderTransaction.feature')


@pytest.fixture
def shared_data():
    return {}       #Return empty dict

#Username, Password are coming feature file in the form of value hence will be written in {}
#Add parsers.parse, so that it can identify {Username} n {Password} are var, else @given will take whole arg as text
@given(parsers.parse('place the order with {Username} and {Password}'))
def place_order(playwright, Username, Password, shared_data):
    #Create empty dict user_credentials, to catch Username n Password
    user_credentials = {}
    #Save Username, Password coming from feature file into user-credentials dict, coz CreateOrder API needs
        #User_credentials as arg.
    user_credentials["userEmail"] = Username
    user_credentials["userPassword"] = Password
    api_calls = APIMethods()
    # Scope of order_id will die outside this method, hence we will create 1 fixture 'shared_data'
    order_id = api_calls.createOrders(playwright, user_credentials)
    shared_data["order_id"] = order_id

@given('the user on landing page')
def user_on_landing_page(browser_selection, shared_data): #We can pass fixture here, so that it will execute 1st
    # Scope of sign_in will die outside this method, hence we will create 1 fixture 'shared_data'
    sign_in = LoginPage(browser_selection)
    sign_in.launch_url()
    #Since shared_data is empty dict, then load 1 key-value data
    shared_data["login_page"] = sign_in #Now sign_in value has been stored in global fixture

@when(parsers.parse('I login into the portal with {Username} and {Password}'))
def user_login_into_portal(Username, Password, shared_data):
    login_page = shared_data["login_page"]      #Take value of login_page (sign_in) into login_page
    dashboard = login_page.login(Username, Password)
    shared_data['dashboard_page'] = dashboard

@when('navigates to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data["dashboard_page"]
    order_details = dashboard_page.click_orders()
    shared_data["order_details_page"] = order_details

@when('selects the orderId')
def select_order_id(shared_data):
    order_details_page = shared_data["order_details_page"]
    order_id = shared_data["order_id"]
    order_history = order_details_page.click_view_for_order(order_id)
    shared_data["order_history_page"] = order_history

@then('order message is successfully displayed')
def order_message_success(shared_data):
    order_history_page = shared_data["order_history_page"]
    order_history_page.verify_order()