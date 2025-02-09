import allure
import pytest
from src.config.settings import RESOURSE_URL
from src.test_data.users_data import data_hunter_preprod
from src.test_data.risks_data import RISK_DATA
from src.config.endpoints import RISKS_ENDPOINT, AUTH_ENDPOINT
from src.utils.assertions import Assertions
from src.utils.api_client import Myrequests


@allure.title("Создание и удаление риска ")
@allure.description("Тестирование создания и удаления нового риска через API")
@pytest.mark.smoke
def test_create_risk(create_headers_for_test):
    with allure.step("Получение заголовков авторизации"):
        print("Получение заголовков авторизации")
        auth_header = create_headers_for_test(url=AUTH_ENDPOINT, payload=data_hunter_preprod)
        print(auth_header)

    with allure.step("Создание нового риска"):
        print("Создание нового риска")
        response2 = Myrequests.post(RISKS_ENDPOINT, auth_header, RISK_DATA)
        risk_id = response2.json().get('id')
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, ["id"])
        print(response2.text)

    with allure.step("Получение информации по созданному риску"):
        print("Получение информации по созданному риску")
        RISKS_ID_ENDPOINT = f"{RESOURSE_URL}api/v1/risks/{risk_id}"
        response3 = Myrequests.get(RISKS_ID_ENDPOINT, auth_header)
        Assertions.assert_code_status(response3, 200)
        # Assertions.assert_json_has_key(response2, ["id", 'author', "description", "place", "category", "status"])
        # не могу понять как валидировать значения в списке
        print(response3.text)

    with allure.step("Удаление риска"):
        print("Удаление риска")
        RISKS_ID_ENDPOINT = f"{RESOURSE_URL}api/v1/risks/{risk_id}"
        response4 = Myrequests.delete(RISKS_ID_ENDPOINT, auth_header)
        Assertions.assert_code_status(response4, 200)

    with allure.step("Проверка удаления риска"):
        print("Проверка удаления риска")
        RISKS_ID_ENDPOINT = f"{RESOURSE_URL}api/v1/risks/{risk_id}"
        response5 = Myrequests.get(RISKS_ID_ENDPOINT, auth_header)
        Assertions.assert_code_status(response5, 404)
        Assertions.assert_json_search_word_in_value(response5, "error", "Not Found")
