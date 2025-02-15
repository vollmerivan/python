import pytest
import requests
from src.config.endpoints import USER_ENDPOINT, AUTH_ENDPOINT
from src.test_data.users_data import create_user_admin
from src.utils import auth_api


"""фикстура создания пользователя"""
@pytest.fixture()
def create_user(create_headers_for_test):
    def _create_user(headers: dict):
        response = requests.post(USER_ENDPOINT, headers=headers, json=create_user_admin)
        return response

    yield _create_user

"""Фикстура авторизации"""
@pytest.fixture()
def create_headers_for_test():
    def _wrapper(url: str, payload: dict):
        if url == AUTH_ENDPOINT:
            token = auth_api.auth_headers(payload=payload)
        else:
            token = auth_api.auth_headers_admin(payload=payload)
        return token

    yield _wrapper



