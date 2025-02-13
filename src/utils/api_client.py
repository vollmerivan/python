import allure
import requests
from src.utils.logger import Logger


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
    def patch(url, headers, data):
        with allure.step("PATCH"):
            Logger.add_request(url, method="PATCH")
            result = requests.put(url, headers=headers, json=data)
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


