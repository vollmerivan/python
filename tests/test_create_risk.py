import allure
from ls.test_data.users_data import data_hunter_preprod
from ls.test_data.risks_data import RISK_DATA
from ls.config.endpoints import RISKS_ENDPOINT
from ls.models.assertions import Assertions
from ls.utils.api_client import Myrequests


@allure.title("Создание риска")
@allure.description("Тестирование создания нового риска через API")
def test_create_risk(auth_api):
    with allure.step("Получение заголовков авторизации"):
        response1 = auth_api.auth_headers(data_hunter_preprod)
        print(response1)

    with allure.step("Создание нового риска"):
        response2 = Myrequests.post(RISKS_ENDPOINT, response1, RISK_DATA)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        print(response2)
        print(response2.text)

    with allure.step("Получение списка рисков"):
        response3 = Myrequests.get(RISKS_ENDPOINT, response1)
        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response2, "id")
        print(response3)
        print(response3.text)
