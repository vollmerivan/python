from requests import Request

from src.api.api_client import api_client
from src.config.endpoints import USER_ENDPOINT, ROLES_USER_ENDPOINT, Admin_USER_ENDPOINT, Admin_role_ENDPOINT, \
    Admin_USER_patch_ENDPOINT
from src.test_data.users_data import UsersData, USER_DATA


def get_users(by_user: UsersData):
    request = Request(url=USER_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def create_user(by_user: UsersData):
    request = Request(url=USER_ENDPOINT, method='post', json=USER_DATA)
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_roles_by_user(by_user: UsersData, user_id: int):
    request = Request(url=ROLES_USER_ENDPOINT.format(user_id=user_id), method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def post_roles_by_user(by_user: UsersData, user_id: int, role_id: dict):
    request = Request(url=ROLES_USER_ENDPOINT.format(user_id=user_id), method='post', json=role_id)
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_any(by_user: UsersData, url: str):
    request = Request(url=url, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_users_admin(by_user: UsersData):
    request = Request(url=Admin_USER_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def patch_user_admin(by_user: UsersData, user_id: int, patch_data: dict):
    request = Request(url=Admin_USER_patch_ENDPOINT.format(user_id=user_id), method='patch', json=patch_data)
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def post_roles_by_user_admin(by_user: UsersData, user_id: int, role_id: dict):
    request = Request(url=Admin_role_ENDPOINT.format(user_id=user_id), method='post', json=role_id)
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_roles_by_user_admin(by_user: UsersData, user_id: int):
    request = Request(url=Admin_role_ENDPOINT.format(user_id=user_id), method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def create_user_admin(by_user: UsersData, user_data: dict):
    request = Request(url=Admin_USER_ENDPOINT, method='post', json=user_data)
    response = api_client.send_request(request=request, by_user=by_user)
    return response
