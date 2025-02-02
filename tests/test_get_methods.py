import requests
import pytest
import allure
from api.auth_api import AuthAPI
from test_data.users_data import data_hunter_preprod, data_admin_preprod, data_rm_preprod
from config.endpoints import (
    RISKS_ENDPOINT, USERS_ME_ENDPOINT, USER_ENDPOINT, PLACES_ENDPOINT, CATEGORIES_ENDPOINT,
    BADGES_ENDPOINT, TASKS_ENDPOINT, SEASONS_ENDPOINT, RISKS_MINE_ENDPOINT, USERS_MANAGED_ENDPOINT, PRIORITIES_ENDPOINT,
    ORG_ENDPOINT, STATISTICS_MINE_ENDPOINT, RATING_ENDPOINT, RISKS_STATUS_EN_ENDPOINT, RISKS_STATUS_RU_ENDPOINT,
    CATEGORIES_MINE_ENDPOINT
)
from models.assertions import Assertions

@pytest.fixture
def auth_api():
    return AuthAPI()

class TestMethodsAPI:

    @allure.title("Проверка методов GET")
    @allure.description("Тестирование запросы GET охотника")
    def test_get_hunter(self, auth_api):


        with allure.step("Получение заголовков авторизации"):
            response1 = auth_api.auth_headers(data_hunter_preprod)


        with allure.step("Отправка запроса USERS_ME_ENDPOINT"):
            response2 = requests.get(USERS_ME_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response2,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса RISKS_MINE_ENDPOINT"):
            response3 = requests.get(RISKS_MINE_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response3,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса PLACES_ENDPOINT"):
            response4 = requests.get(PLACES_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response4,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса CATEGORIES_ENDPOINT"):
            response5 = requests.get(CATEGORIES_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response5,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса STATISTICS_MINE_ENDPOINT"):
            response6 = requests.get(STATISTICS_MINE_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response6,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса RATING_ENDPOINT"):
            response7 = requests.get(RATING_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response7,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса TASKS_ENDPOINT"):
            response8 = requests.get(TASKS_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response8,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса PRIORITIES_ENDPOINT"):
            response9 = requests.get(PRIORITIES_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response9,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса SEASONS_ENDPOINT"):
            response10 = requests.get(SEASONS_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response10,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса RISKS_STATUS_RU_ENDPOINT"):
            response11 = requests.get(RISKS_STATUS_RU_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response11,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса RISKS_STATUS_EN_ENDPOINT"):
            response12 = requests.get(RISKS_STATUS_EN_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response12,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"




    @allure.title("Проверка методов GET")
    @allure.description("Тестирование запросы GET админ")
    def test_get_admin(self, auth_api):


        with allure.step("Получение заголовков авторизации"):
            response1 = auth_api.auth_headers(data_admin_preprod)

        with allure.step("Отправка запроса USERS_ME_ENDPOINT"):
            response2 = requests.get(USERS_ME_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response2,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса USER_ENDPOINT"):
            response3 = requests.get(USER_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response3,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса ORG_ENDPOINT"):
            response4 = requests.get(ORG_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response4,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса BADGES_ENDPOINT"):
            response5 = requests.get(BADGES_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response5,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"

    @allure.title("Проверка методов GET")
    @allure.description("Тестирование запросы GET риск менеджер")
    def test_get_rm(self, auth_api):
        with allure.step("Получение заголовков авторизации"):
            response1 = auth_api.auth_headers(data_rm_preprod)

        with allure.step("Отправка запроса USERS_ME_ENDPOINT"):
            response2 = requests.get(USERS_ME_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response2,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса USER_ENDPOINT"):
            response3 = requests.get(USER_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response3,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса USERS_MANAGED_ENDPOINT"):
            response4 = requests.get(USERS_MANAGED_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response4,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса RISKS_ENDPOINT"):
            response5 = requests.get(RISKS_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response5,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса CATEGORIES_MINE_ENDPOINT"):
            response6 = requests.get(CATEGORIES_MINE_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response6,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса CATEGORIES_ENDPOINT"):
            response7 = requests.get(CATEGORIES_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response7,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса TASKS_ENDPOINT"):
            response8 = requests.get(TASKS_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response8,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"