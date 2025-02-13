import allure
import pytest
from src.test_data.users_data import data_hunter_preprod, data_admin_preprod, data_rm_preprod
from src.config.endpoints import (
    RISKS_ENDPOINT, USERS_ME_ENDPOINT, USER_ENDPOINT, PLACES_ENDPOINT, CATEGORIES_ENDPOINT,
    BADGES_ENDPOINT, TASKS_ENDPOINT, SEASONS_ENDPOINT, RISKS_MINE_ENDPOINT, USERS_MANAGED_ENDPOINT, PRIORITIES_ENDPOINT,
    ORG_ENDPOINT, STATISTICS_MINE_ENDPOINT, RATING_ENDPOINT, RISKS_STATUS_EN_ENDPOINT, RISKS_STATUS_RU_ENDPOINT,
    CATEGORIES_MINE_ENDPOINT, AUTH_ENDPOINT)
from src.utils.assertions import Assertions
from src.utils.api_client import Myrequests


@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET охотника")
@pytest.mark.smoke
def test_get_hunter(create_headers_for_test):
    with allure.step("Получение заголовков авторизации"):
        auth_header = create_headers_for_test(url=AUTH_ENDPOINT, payload=data_hunter_preprod)

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
            response2 = Myrequests.get(endpoint, headers=auth_header)
            Assertions.assert_code_status(response2, 200)
            print(f"Запрос {endpoint} успешен")


@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET админ")
@pytest.mark.smoke
def test_get_admin(create_headers_for_test):
    with allure.step("Получение заголовков авторизации"):
        auth_header = create_headers_for_test(url=AUTH_ENDPOINT, payload=data_admin_preprod)

    endpoints_list = [USERS_ME_ENDPOINT,
                      USER_ENDPOINT,
                      ORG_ENDPOINT,
                      BADGES_ENDPOINT
                      ]

    for endpoint in endpoints_list:
        with allure.step(f"Отправка запроса {endpoint}"):
            response2 = Myrequests.get(endpoint, headers=auth_header)
            Assertions.assert_code_status(response2, 200)
            print(f"Запрос {endpoint} успешен")


@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET риск менеджер")
@pytest.mark.smoke
def test_get_rm(create_headers_for_test):
    with allure.step("Получение заголовков авторизации"):
        auth_header = create_headers_for_test(url=AUTH_ENDPOINT, payload=data_rm_preprod)

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
            response2 = Myrequests.get(endpoint, headers=auth_header)
            Assertions.assert_code_status(response2, 200)
            print(f"Запрос {endpoint} успешен")
