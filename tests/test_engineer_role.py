import pytest
import allure
from ls.config.settings import RESOURSE_URL
from ls.test_data.users_data import data_engineer_preprod, data_admin_preprod, data_rm_preprod
from ls.config.endpoints import (
    RISKS_ENDPOINT, USERS_ME_ENDPOINT, USER_ENDPOINT, PLACES_MINE_ENDPOINT, CATEGORIES_ENDPOINT,
    TASKS_ENDPOINT, RISKS_STATUS_EN_ENDPOINT, RISKS_STATUS_RU_ENDPOINT, EVENTS_STATUS_RU_ENDPOINT, EVENTS_STATUS_EN_ENDPOINT,
    SEASONS_MINE_ENDPOINT, ROLES_POST_ENDPOINT, ROLES_ENDPOINT, EVENTS_ENDPOINT,
    RISKS_ID_EVENT_ENDPOINT, RISKS_ID_ENDPOINT)
from ls.utils.assertions import Assertions
from ls.test_data.events_data import EVENT_DATA_GET, EVENT_DATA_SET, EVENT_DATA
from ls.utils.api_client import Myrequests


@allure.title("Тест на создание роли инженера")
@allure.description("Проверка успешного присвоения роли инженера и получения списка ролей")
def test_post_engineer_role(auth_api):
        with allure.step("Получение заголовков авторизации для администратора"):
            response1 = auth_api.auth_headers(data_admin_preprod)

        with (allure.step("Присвоения роли инженера")):
            payload = {'id': 8}
            response2 = Myrequests.post(ROLES_POST_ENDPOINT, headers=response1, json=payload)
            assert response2.status_code in (200, 409), f"Ожидалось 200 или 409, но получен: {response2.status_code}"

        with allure.step("Получения списка ролей"):
            response3 = Myrequests.get(ROLES_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response3, 200)

@allure.title("Тест на создание мероприятия")
@allure.description("Проверка успешного создания мероприятия и запись его ИД в переменную")
@pytest.fixture
def test_post_event(auth_api):
        response1 = auth_api.auth_headers(data_rm_preprod)
        response2 = Myrequests.post(RISKS_ID_EVENT_ENDPOINT, headers=response1, json=EVENT_DATA)
        Assertions.assert_code_status(response2,200)

        eventId = response2.json().get('id') # Сохраняем eventId в атрибут класса
        return eventId


@allure.title("Тест на получение данных инженера")
@allure.description("Проверка доступности различных API для пользователя-инженера")
def test_get_engineer(auth_api, test_post_event):
    eventId = test_post_event
    EVENTS_ID_HISTORY_ENDPOINT = f"{RESOURSE_URL}api/v1/events/{eventId}/history"

    with allure.step("Получение заголовков авторизации для инженера"):
        response1 = auth_api.auth_headers(data_engineer_preprod)

    endpoints_list = [RISKS_ENDPOINT,
                      USERS_ME_ENDPOINT,
                      USER_ENDPOINT,
                      PLACES_MINE_ENDPOINT,
                      CATEGORIES_ENDPOINT,
                      TASKS_ENDPOINT,
                      RISKS_STATUS_EN_ENDPOINT,
                      RISKS_STATUS_RU_ENDPOINT,
                      EVENTS_STATUS_RU_ENDPOINT,
                      EVENTS_STATUS_EN_ENDPOINT,
                      SEASONS_MINE_ENDPOINT,
                      EVENTS_ENDPOINT,
                      RISKS_ID_ENDPOINT,
                      RISKS_ID_EVENT_ENDPOINT
                      ]

    for endpoint in endpoints_list:
        with allure.step(f"Отправка запроса {endpoint}"):
            response2 = Myrequests.get(endpoint, headers=response1)
            Assertions.assert_code_status(response2, 200)
            print(f"Запрос {endpoint} успешен")

    with allure.step("Отправка запроса EVENTS_ID_ENDPOINT"):
        EVENTS_ID_ENDPOINT = f"{RESOURSE_URL}api/v1/events/{eventId}/"
        response4 = Myrequests.get(EVENTS_ID_ENDPOINT, headers=response1)
        Assertions.assert_code_status(response4, 200)
        print(f"Запрос EVENTS_ID_ENDPOINT успешен")

    with allure.step("Отправка запроса EVENTS_ID_HISTORY_ENDPOINT"):
        response15 = Myrequests.get(EVENTS_ID_HISTORY_ENDPOINT, headers=response1)
        Assertions.assert_code_status(response15, 200)

    with allure.step("Отправка PUT запроса EVENTS_ID_ENDPOINT"):
        response19 = Myrequests.put(EVENTS_ID_ENDPOINT, headers=response1, json=EVENT_DATA_SET)
        Assertions.assert_code_status(response19, 200)

    with allure.step("Отправка PATCH запроса EVENTS_ID_ENDPOINT"):
        response20 = Myrequests.patch(EVENTS_ID_ENDPOINT, headers=response1, json=EVENT_DATA_GET)
        Assertions.assert_code_status(response20, 200)

    with allure.step("Отправка запроса USER_ENDPOINT"):
        response21 = Myrequests.get(USER_ENDPOINT, headers=response1)
        Assertions.assert_code_status(response21, 200)
