import allure
import pytest
from ls.config.settings import RESOURSE_URL
from ls.test_data.users_data import data_hunter_preprod
from ls.test_data.risks_data import RISK_DATA
from ls.config.endpoints import RISKS_ENDPOINT
from ls.utils.assertions import Assertions
from ls.utils.api_client import Myrequests


@allure.title("Создание и удаление риска ")
@allure.description("Тестирование создания и удаления нового риска через API")
@pytest.mark.smoke
def test_create_risk(auth_api):
    with allure.step("Получение заголовков авторизации"):
        print("Получение заголовков авторизации")
        response1 = auth_api.auth_headers(data_hunter_preprod)
        print(response1)

    with allure.step("Создание нового риска"):
        print("Создание нового риска")
        response2 = Myrequests.post(RISKS_ENDPOINT, response1, RISK_DATA)
        risk_id = response2.json().get('id')
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, ["id"])
        print(response2.text)

    with allure.step("Получение информации по созданному риску"):
        print("Получение информации по созданному риску")
        RISKS_ID_ENDPOINT = f"{RESOURSE_URL}api/v1/risks/{risk_id}"
        response3 = Myrequests.get(RISKS_ID_ENDPOINT, response1)
        Assertions.assert_code_status(response3, 200)
        # Assertions.assert_json_has_key(response2, ["id", 'author', "description", "place", "category", "status"])
        # не могу понять как валидировать значения в списке
        print(response3.text)

    with allure.step("Удаление риска"):
        print("Удаление риска")
        RISKS_ID_ENDPOINT = f"{RESOURSE_URL}api/v1/risks/{risk_id}"
        response4 = Myrequests.delete(RISKS_ID_ENDPOINT, response1)
        Assertions.assert_code_status(response4, 200)

    with allure.step("Проверка удаления риска"):
        print("Проверка удаления риска")
        RISKS_ID_ENDPOINT = f"{RESOURSE_URL}api/v1/risks/{risk_id}"
        response5 = Myrequests.get(RISKS_ID_ENDPOINT, response1)
        Assertions.assert_code_status(response5, 404)
        Assertions.assert_json_search_word_in_value(response5, "error", "Not Found")
