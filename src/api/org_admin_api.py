from requests import Request

from src.api.api_client import api_client
from src.config.endpoints import ORG_ENDPOINT, ORG_ENDPOINT_ID
from src.test_data.users_data import UsersData



def get_organizations(by_user: UsersData):
    request = Request(url=ORG_ENDPOINT, method='get')
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def create_organization(by_user: UsersData, org_data: dict):
    request = Request(url=ORG_ENDPOINT, method='post', json=org_data)
    response = api_client.send_request(request=request, by_user=by_user)
    return response

def patch_org_by_id(by_user: UsersData, organizationId: int, org_data: dict):
    request = Request(url=ORG_ENDPOINT_ID.format(organizationId=organizationId), method='patch')
    response = api_client.send_request(request=request, by_user=by_user)
    return response
