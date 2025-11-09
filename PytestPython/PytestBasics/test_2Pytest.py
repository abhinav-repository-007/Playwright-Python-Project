# Pytest Basics
import pytest

@pytest.fixture(scope='module')
def preWork():
    print("Module : I ran at the very first time before any test file runs.")
    return "pass"

@pytest.fixture(scope='function')
def secondWork():
    print("Function : I ran at the very first time before any test file runs.")
    yield                       # It will pause here n go to test fun again, n execute, then back n execute post yield commands
                                # Yield is seperator b/w pre setup and post fun execution completion
    print("Tear down function")

def test_thirdFunction(preWork, secondWork):
    print("Third function execution.")
    assert preWork == "pass"

def test_forthFunction(preWork, secondWork):       # Run icon, as it is a Pytest function
    print("Forth function execution.")



