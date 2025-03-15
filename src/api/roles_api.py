from urllib.request import Request

from src.config.endpoints import ROLES_ENDPOINT
from src.test_data.users_data import UsersData
from src.api.api_client import api_client


def get_roles(by_user: UsersData):
    request = Request(url=ROLES_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


