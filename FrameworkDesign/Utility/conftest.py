import pytest


@pytest.fixture(scope="session")
def user_credentials(request): #global request
    return request.param #Check whether any parameter is attached to the test, and return
