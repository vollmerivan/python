from requests import Request

from src.api.api_client import api_client
from src.test_data.risks_data import RISK_DATA
from src.test_data.users_data import UsersData
from src.config.endpoints import RISKS_ENDPOINT, RISKS_ID_ENDPOINT, RISKS_MINE_ENDPOINT, RISKS_ID_HISTORY, \
    RISKS_EXPORT_ENDPOINT


def get_risks(by_user: UsersData):
    request = Request(url=RISKS_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def create_risk(by_user: UsersData):
    request = Request(url=RISKS_ENDPOINT, method='post', json=RISK_DATA)
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_risk_by_id(by_user: UsersData, risk_id: int):
    request = Request(url=RISKS_ID_ENDPOINT.format(risk_id=risk_id), method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def delete_risk_by_id(by_user: UsersData, risk_id: int):
    request = Request(url=RISKS_ID_ENDPOINT.format(risk_id=risk_id), method='delete')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def patch_risk_by_id(by_user: UsersData, risk_id: int):
    request = Request(url=RISKS_ID_ENDPOINT.format(risk_id=risk_id), method='patch')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_risks_mine(by_user: UsersData):
    request = Request(url=RISKS_MINE_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


def get_risk_history(by_user: UsersData):
    request = Request(url=RISKS_ID_HISTORY, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response


# Сохранение в файл..........
def get_risk_export(by_user: UsersData):
    request = Request(url=RISKS_EXPORT_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response
