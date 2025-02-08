import pytest
import requests
from ls.config.endpoints import USER_ENDPOINT, Admin_AUTH_ENDPOINT, AUTH_ENDPOINT
from ls.test_data.users_data import create_user_admin
from ls.utils.auth_api import AuthAPIadmin, AuthAPI


@pytest.fixture(scope="session")
def auth_api():
    return AuthAPI()


@pytest.fixture(scope="session")
def auth_api_admin():
    return AuthAPIadmin()



"""фикстура создания пользователя"""
# @pytest.fixture(scope="session")
# def create_user():
#     def _create_user(auth_api):
#         response = requests.post(USER_ENDPOINT, headers=auth_api, json=create_user_admin)
#
#     return _create_user

"""Фикстура как фабрика"""
# @pytest.fixture(scope="session")
# def create_headers_for_test():
#     def _wrapper(url: str):
#         if AUTH_ENDPOINT:
#             token = auth_api()
#         else:
#             token = auth_api_admin()
#         return {'Authorization': f"Bearer {token}"}
#
#     yield _wrapper



