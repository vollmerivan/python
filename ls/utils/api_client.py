import requests


class APIClient:
    @staticmethod
    def get(url):
        return requests.get(url)

    @staticmethod
    def post(url, data):
        return requests.post(url, json=data)

    @staticmethod
    def put(url, data):
        return requests.put(url, json=data)

    @staticmethod
    def delete(url):
        return requests.delete(url)
