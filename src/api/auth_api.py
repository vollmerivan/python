from requests import Request

from src.api.api_client import api_client
from src.config.endpoints import AUTH_ENDPOINT
from src.test_data.users_data import UsersData


def auth(by_user: UsersData):
    request = Request(url=AUTH_ENDPOINT, method='post')
    response = api_client.send_request(request=request, by_user=by_user)
    return response
