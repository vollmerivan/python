import requests
import allure
import json
from config.endpoints import AUTH_ENDPOINT, Admin_AUTH_ENDPOINT
from models.assertions import Assertions


class AuthAPI:
    @allure.step("Выполнение запроса на логин с данными: {payload}")
    def auth_headers(self, payload):
        with allure.step("Отправка POST запроса на авторизацию"):
            response = requests.post(AUTH_ENDPOINT, json=payload)
            response_dict = response.json()
            token = response.json().get('token')
            Assertions.assert_json_has_key(response, 'token')
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
        authorization = {'Authorization': f"Bearer {token}"}
        return authorization



class AuthAPIadmin:
    @allure.step("Выполнение запроса на логин с данными: {payload}")
    def auth_headers_admin(self, payload):
        with allure.step("Отправка POST запроса на авторизацию"):
            response1 = requests.post(Admin_AUTH_ENDPOINT, json=payload)

            response_dict = response1.json()
            token = response1.json().get('token')
            Assertions.assert_json_has_key(response1, 'token')
            allure.attach(
                json.dumps(payload, ensure_ascii=False, indent=2),
                name="Запрос (Payload)",
                attachment_type=allure.attachment_type.JSON
            )
        with allure.step("Получение ответа от сервера"):
            allure.attach(
                response1.text,
                name="Ответ (Response)",
                attachment_type=allure.attachment_type.JSON
            )
        authorization = {'Authorization': f"Bearer {token}"}

        return authorization