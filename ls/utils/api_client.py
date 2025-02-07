import allure
import requests
from ls.utils.logger import Logger


class Myrequests:
    headers = None



    @staticmethod
    def get(url, headers):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=headers)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, headers, data):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, headers=headers, json=data)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, headers, data):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, headers=headers, json=data)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, headers):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, headers=headers)
            Logger.add_response(result)
            return result


    # @staticmethod
    # def post(url, headers, data):
    #     return Myrequests._send(url, headers, data, 'POST')
    #
    # @staticmethod
    # def get(url, headers):
    #     return Myrequests._send(url, headers, 'GET')

    # @staticmethod
    # def _send(url:str, headers: dict, data: dict, method: str):
    #     if headers is None:
    #         data = {}
    #
    #     if method = 'GET':
    #         response = requests.get(url, headers=headers)
    #     elif method = 'POST':
    #         response = requests.post(url, data=data, headers=headers)
    #     elif method = 'PUT':
    #         response = requests.put(url, data=data, headers=headers)
    #     elif method = 'PATCH':
    #         response = requests.patch(url, data=data, headers=headers)
    #     elif method = 'DELETE':
    #         response = requests.delete(url, data=data, headers=headers)
    #     else:
    #         raise Exception(f"Не верный HTTP '{method}")
    #
    #     return response
