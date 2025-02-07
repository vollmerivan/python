import requests
import allure
from test_data.users_data import data_hunter_preprod, data_admin_preprod, data_rm_preprod
from config.endpoints import (
    RISKS_ENDPOINT, USERS_ME_ENDPOINT, USER_ENDPOINT, PLACES_ENDPOINT, CATEGORIES_ENDPOINT,
    BADGES_ENDPOINT, TASKS_ENDPOINT, SEASONS_ENDPOINT, RISKS_MINE_ENDPOINT, USERS_MANAGED_ENDPOINT, PRIORITIES_ENDPOINT,
    ORG_ENDPOINT, STATISTICS_MINE_ENDPOINT, RATING_ENDPOINT, RISKS_STATUS_EN_ENDPOINT, RISKS_STATUS_RU_ENDPOINT,
    CATEGORIES_MINE_ENDPOINT)
from models.assertions import Assertions


@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET охотника")
def test_get_hunter(auth_api):
    with allure.step("Получение заголовков авторизации"):
        response1 = auth_api.auth_headers(data_hunter_preprod)

    endpoints_list = [USERS_ME_ENDPOINT,
                      RISKS_MINE_ENDPOINT,
                      PLACES_ENDPOINT,
                      CATEGORIES_ENDPOINT,
                      STATISTICS_MINE_ENDPOINT,
                      RATING_ENDPOINT,
                      TASKS_ENDPOINT,
                      PRIORITIES_ENDPOINT,
                      SEASONS_ENDPOINT,
                      RISKS_STATUS_RU_ENDPOINT,
                      RISKS_STATUS_EN_ENDPOINT]

    for endpoint in endpoints_list:
        with allure.step(f"Отправка запроса {endpoint}"):
            response2 = requests.get(endpoint, headers=response1)
            Assertions.assert_code_status(response2, 200)
            print(f"Запрос {endpoint} успешен")


@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET админ")
def test_get_admin(auth_api):
    with allure.step("Получение заголовков авторизации"):
        response1 = auth_api.auth_headers(data_admin_preprod)

    endpoints_list = [USERS_ME_ENDPOINT,
                      USER_ENDPOINT,
                      ORG_ENDPOINT,
                      BADGES_ENDPOINT
                      ]

    for endpoint in endpoints_list:
        with allure.step(f"Отправка запроса {endpoint}"):
            response2 = requests.get(endpoint, headers=response1)
            Assertions.assert_code_status(response2, 200)
            print(f"Запрос {endpoint} успешен")


@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET риск менеджер")
def test_get_rm(auth_api):
    with allure.step("Получение заголовков авторизации"):
        response1 = auth_api.auth_headers(data_rm_preprod)

    endpoints_list = [USERS_ME_ENDPOINT,
                      USER_ENDPOINT,
                      USERS_MANAGED_ENDPOINT,
                      RISKS_ENDPOINT,
                      CATEGORIES_MINE_ENDPOINT,
                      CATEGORIES_ENDPOINT,
                      TASKS_ENDPOINT
                      ]

    for endpoint in endpoints_list:
        with allure.step(f"Отправка запроса {endpoint}"):
            response2 = requests.get(endpoint, headers=response1)
            Assertions.assert_code_status(response2, 200)
            print(f"Запрос {endpoint} успешен")
