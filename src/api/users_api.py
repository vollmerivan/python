from requests import Request

from src.api.api_client import api_client
from src.config.endpoints import USER_ENDPOINT
from src.test_data.users_data import UsersData, USER_DATA


def get_users(by_user: UsersData):
    request = Request(url=USER_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def create_user(by_user: UsersData):
    request = Request(url=USER_ENDPOINT, method='post', json=USER_DATA)
    response = api_client.send_request(request=request, by_user=by_user)
    return response