import requests
import allure
import json
from config.endpoints import AUTH_ENDPOINT, Admin_AUTH_ENDPOINT
from models.assertions import Assertions


class AuthAPI:
    @allure.step("Выполнение запроса на логин с данными: {payload}")
    def login(self, payload):
        with allure.step("Отправка POST запроса на авторизацию"):
            response = requests.post(AUTH_ENDPOINT, json=payload)
            allure.attach(
                json.dumps(payload, ensure_ascii=False, indent=2),
                name="Запрос (Payload)",
                attachment_type=allure.attachment_type.JSON
            )
        with allure.step("Получение ответа от сервера"):
            allure.attach(
                response.text,
                name="Ответ (Response)",
                attachment_type=allure.attachment_type.JSON
            )
        return response

    def auth_headers(self, payload):
        response1 = requests.post(AUTH_ENDPOINT, json=payload)

        response_dict = response1.json()
        token = response1.json().get('token')
        Assertions.assert_json_has_key(response1, 'token')

        authorization = {'Authorization': f"Bearer {token}"}

        return authorization

class AuthAPIadmin:
    @allure.step("Выполнение запроса на логин с данными: {payload}")
    def login_admin(self, payload):
        with allure.step("Отправка POST запроса на авторизацию"):
            response = requests.post(Admin_AUTH_ENDPOINT, json=payload)
            allure.attach(
                json.dumps(payload, ensure_ascii=False, indent=2),
                name="Запрос (Payload)",
                attachment_type=allure.attachment_type.JSON
            )
        with allure.step("Получение ответа от сервера"):
            allure.attach(
                response.text,
                name="Ответ (Response)",
                attachment_type=allure.attachment_type.JSON
            )
        return response

    def auth_headers_admin(self, payload):
        response1 = requests.post(Admin_AUTH_ENDPOINT, json=payload)

        response_dict = response1.json()
        token = response1.json().get('token')
        Assertions.assert_json_has_key(response1, 'token')

        authorization = {'Authorization': f"Bearer {token}"}

        return authorization



