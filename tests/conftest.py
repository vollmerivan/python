import pytest
from api.auth_api import AuthAPIadmin, AuthAPI


@pytest.fixture(scope="session")
def auth_api():
    return AuthAPI()


@pytest.fixture(scope="session")
def auth_api_admin():
    return AuthAPIadmin()
