import pytest
import requests
from ls.config.endpoints import USER_ENDPOINT
from ls.test_data.users_data import create_user_admin
from ls.api.auth_api import AuthAPIadmin, AuthAPI


@pytest.fixture(scope="session")
def auth_api():
    return AuthAPI()


@pytest.fixture(scope="session")
def auth_api_admin():
    return AuthAPIadmin()


@pytest.fixture(scope="session")
def create_user():
    def _create_user(auth_api):
        response = requests.post(USER_ENDPOINT, headers=auth_api, json=create_user_admin)
    return _create_user

# @pytest.fixture(scope="session")
# def auth_token():
#     def _wrapper():
#     if url:
#         token = auth_headers(url)
#     return {'Authorization': f"Bearer {token}"}
#
# yield