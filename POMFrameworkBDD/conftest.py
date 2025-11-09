import pytest

#This method is to provide definition for --browser_name
#This method is pre-defined in pytest doc,just copy n modify accordingly.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser selection"
    )
    #Definition for --url_name
    # parser.addoption(
    #     "--url_name", action="store", default="https://rahulshettyacademy.com/client/", help="Server selection"
    # )

@pytest.fixture(scope="session")
def user_credentials(request):  #global request
    return request.param  #Check whether any parameter is attached to the test, and return


#We want to start from starting the browser, but scope='session' was storing token from 1st run and was trying to
#login 2nd time with new creds, but since we already logged in, hence login screen was missing.
#Thats y scope='session' is not required.
@pytest.fixture
def browser_selection(playwright, request):
    #To take browser name dynamically from terminal, define the browser_name
    browser_name = request.config.getoption("--browser_name")  #Identify browser name from terminal with "--browser_name"
    #"--browser-name" is a user defined name
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    # url_name = request.config.getoption("--url_name")

    context = browser.new_context()
    page = context.new_page()

    #Take dynamically url name from terminal, just like browser name
    # Paste here the url step copied from login.navigate()
    # page.goto(url_name)

    yield page  #Yeild works as return here
    context.close()
    browser.close()
