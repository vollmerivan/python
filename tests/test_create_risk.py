import requests
import allure
from ls.test_data.users_data import data_hunter_preprod
from ls.test_data.risks_data import RISK_DATA
from ls.config.endpoints import RISKS_ENDPOINT
from ls.models.assertions import Assertions


@allure.title("Создание риска")
@allure.description("Тестирование создания нового риска через API")
def test_create_risk(auth_api):

        with allure.step("Получение заголовков авторизации"):
            response1 = auth_api.auth_headers(data_hunter_preprod)

            print(response1)

        with allure.step("Создание нового риска"):
            response2 = requests.post(RISKS_ENDPOINT, headers=response1, json=RISK_DATA)
            Assertions.assert_code_status(response2, 200)
            Assertions.assert_json_has_key(response2, "id")

        with allure.step("Получение списка рисков"):
            response3 = requests.get(RISKS_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response3, 200)








