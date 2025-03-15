from requests import Request

from src.api.api_client import api_client
from src.config.endpoints import RISKS_ID_EVENT_ENDPOINT, EVENTS_ENDPOINT, EVENTS_ID_ENDPOINT, \
    EVENTS_ID_HISTORY_ENDPOINT
from src.test_data.users_data import UsersData


def get_events(by_user: UsersData):
    request = Request(url=EVENTS_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def create_event_by_risk_id(by_user: UsersData, risk_id: int, event_data: dict):
    request = Request(url=RISKS_ID_EVENT_ENDPOINT.format(risk_id=risk_id), method='post', json=event_data)
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def get_event_by_risk_id(by_user: UsersData, risk_id: int):
    request = Request(url=RISKS_ID_EVENT_ENDPOINT.format(risk_id=risk_id), method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def patch_event_by_id(by_user: UsersData, event_id: int, event_data: dict):
    request = Request(url=EVENTS_ID_ENDPOINT.format(event_id=event_id), method='patch', json=event_data)
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def get_event_by_id(by_user: UsersData, event_id: int):
    request = Request(url=EVENTS_ID_ENDPOINT.format(event_id=event_id), method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def get_event_history_by_id(by_user: UsersData, event_id: int):
    request = Request(url=EVENTS_ID_HISTORY_ENDPOINT.format(event_id=event_id), method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def put_event_by_id(by_user: UsersData, event_id: int, event_data: dict):
    request = Request(url=EVENTS_ID_ENDPOINT.format(event_id=event_id), method='put', json=event_data)
    response = api_client.send_request(request=request, by_user=by_user)
    return response

