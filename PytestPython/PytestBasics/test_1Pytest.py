# Pytest Basics
import pytest

# Create Pytest function by just adding 'test_' before function name, which will help to identify test functions

@pytest.fixture(scope='module')      # pytest fixture will execute at the very first time only before 1st test run.
def preWork():
    print("I run before any test function runs.")

# mention fixture method as parameter in test method to make relation b/w test n fixture functions.
def test_firstFunction(preWork):
    print("First function execution.")

def test_secondFunction(preSetupWork):       # Run icon, as it is a Pytest function
    print("Seconds function execution.")

