import requests
import allure
import json
from src.config.endpoints import AUTH_ENDPOINT, Admin_AUTH_ENDPOINT
from src.utils.assertions import Assertions


@allure.step("Выполнение запроса на логин с данными: {payload}")
def auth_headers(payload):
    with allure.step("Отправка POST запроса на авторизацию"):
        response = requests.post(AUTH_ENDPOINT, json=payload)
        response_dict = response.json()
        token = response.json().get('token')
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_token(response, 'token')
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


@allure.step("Выполнение запроса на логин с данными: {payload}")
def auth_headers_admin(payload):
    with allure.step("Отправка POST запроса на авторизацию"):
        response1 = requests.post(Admin_AUTH_ENDPOINT, json=payload)

        response_dict = response1.json()
        token = response1.json().get('token')
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_token(response1, 'token')
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
