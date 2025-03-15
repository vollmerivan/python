from requests import Request

from src.api.api_client import api_client
from src.config.endpoints import CATEGORIES_ENDPOINT
from src.test_data.other_data import category_data
from src.test_data.users_data import UsersData


def get_categories(by_user: UsersData):
    request = Request(url=CATEGORIES_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_categories_mine(by_user: UsersData):
    request = Request(url=CATEGORIES_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def create_categories(by_user: UsersData):
    request = Request(url=CATEGORIES_ENDPOINT, method='post', json=category_data)
    response = api_client.send_request(request=request, by_user=by_user)
    return response