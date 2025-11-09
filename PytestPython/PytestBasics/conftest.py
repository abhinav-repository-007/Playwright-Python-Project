import pytest


@pytest.fixture(scope='session')      # pytest fixture will execute at the very first time only before 1st test run.
def preSetupWork():
    print("I run at the very 1st time when session starts before any test file runs.")

