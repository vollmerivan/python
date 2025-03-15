from requests import Request

from src.api.api_client import api_client
from src.config.endpoints import PLACES_ENDPOINT, PLACES_MINE_ENDPOINT
from src.test_data.other_data import place_data
from src.test_data.users_data import UsersData


def get_places(by_user: UsersData):
    request = Request(url=PLACES_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_places_mine(by_user: UsersData):
    request = Request(url=PLACES_MINE_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def create_places(by_user: UsersData) -> object:
    request = Request(url=PLACES_ENDPOINT, method='post', json=place_data)
    response = api_client.send_request(request=request, by_user=by_user)
    return response