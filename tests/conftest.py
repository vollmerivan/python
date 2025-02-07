import pytest
from api.auth_api import AuthAPI

@pytest.fixture
def auth_api():
    return AuthAPI()