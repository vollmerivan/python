import allure
import pytest

from src.api.users_api import get_any
from src.test_data.users_data import DATA_ADMIN_PREPROD, DATA_RM_PREPROD, DATA_HUNTER
from src.config.endpoints import (
    RISKS_ENDPOINT, USERS_ME_ENDPOINT, USER_ENDPOINT, PLACES_ENDPOINT, CATEGORIES_ENDPOINT,
    BADGES_ENDPOINT, TASKS_ENDPOINT, SEASONS_ENDPOINT, RISKS_MINE_ENDPOINT, USERS_MANAGED_ENDPOINT, PRIORITIES_ENDPOINT,
    ORG_ENDPOINT, STATISTICS_MINE_ENDPOINT, RATING_ENDPOINT, RISKS_STATUS_EN_ENDPOINT, RISKS_STATUS_RU_ENDPOINT,
    CATEGORIES_MINE_ENDPOINT)
from src.utils.assertions import Assertions



@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET охотника")
@pytest.mark.smoke
def test_get_hunter(create_headers_for_test):

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
            response = get_any(url=endpoint, by_user=DATA_HUNTER)
            Assertions.assert_code_status(response, 200)
            print(f"Запрос {endpoint} успешен")


@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET админ")
@pytest.mark.smoke
def test_get_admin(create_headers_for_test):

    endpoints_list = [USERS_ME_ENDPOINT,
                      USER_ENDPOINT,
                      ORG_ENDPOINT,
                      BADGES_ENDPOINT
                      ]

    for endpoint in endpoints_list:
        with allure.step(f"Отправка запроса {endpoint}"):
            response = get_any(url=endpoint, by_user=DATA_ADMIN_PREPROD)
            Assertions.assert_code_status(response, 200)
            print(f"Запрос {endpoint} успешен")


@allure.title("Проверка методов GET")
@allure.description("Тестирование запросы GET риск менеджер")
@pytest.mark.smoke
def test_get_rm(create_headers_for_test):

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
            response = get_any(url=endpoint, by_user=DATA_RM_PREPROD)
            Assertions.assert_code_status(response, 200)
            print(f"Запрос {endpoint} успешен")
