import requests
import pytest
import allure
from api.auth_api import AuthAPI
from config.settings import RESOURSE_URL
from test_data.users_data import data_engineer_preprod, data_admin_preprod, data_rm_preprod
from config.endpoints import (
    RISKS_ENDPOINT, USERS_ME_ENDPOINT, USER_ENDPOINT, PLACES_MINE_ENDPOINT, CATEGORIES_ENDPOINT,
    TASKS_ENDPOINT, RISKS_STATUS_EN_ENDPOINT, RISKS_STATUS_RU_ENDPOINT, EVENTS_STATUS_RU_ENDPOINT, EVENTS_STATUS_EN_ENDPOINT,
    SEASONS_MINE_ENDPOINT, ROLES_POST_ENDPOINT, ROLES_ENDPOINT, EVENTS_ENDPOINT,
    RISKS_ID_EVENT_ENDPOINT, RISKS_ID_ENDPOINT)
from models.assertions import Assertions
from test_data.events_data import EVENT_DATA_GET, EVENT_DATA_SET, EVENT_DATA


@pytest.fixture
def auth_api():
    return AuthAPI()


class TestAPIEngineer:

    @allure.title("Тест на создание роли инженера")
    @allure.description("Проверка успешного присвоения роли инженера и получения списка ролей")
    def test_post_engineer_role(self, auth_api):
        with allure.step("Получение заголовков авторизации для администратора"):
            response1 = auth_api.auth_headers(data_admin_preprod)

        with (allure.step("Присвоения роли инженера")):
            payload = {'id': 8}
            response2 = requests.post(ROLES_POST_ENDPOINT, headers=response1, json=payload)
            assert response2.status_code in (200, 409), f"Ожидалось 200 или 409, но получен: {response2.status_code}"

        with allure.step("Получения списка ролей"):
            response3 = requests.get(ROLES_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response3, 200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"

    @allure.title("Тест на создание мероприятия")
    @allure.description("Проверка успешного создания мероприятия и запись его ИД в переменную")
    @pytest.fixture
    def test_post_event(self, auth_api):
        response1 = auth_api.auth_headers(data_rm_preprod)
        response2 = requests.post(RISKS_ID_EVENT_ENDPOINT, headers=response1, json=EVENT_DATA)
        (Assertions.assert_code_status(response2,200),
         "Ожидался статус {expected_status}, но получен {response.status_code}\n")

        # Сохраняем eventId в атрибут класса
        eventId = response2.json().get('id')
        return eventId
    @allure.title("Тест на получение данных инженера")
    @allure.description("Проверка доступности различных API для пользователя-инженера")
    def test_get_engineer(self, auth_api, test_post_event):
        eventId = test_post_event
        EVENTS_ID_HISTORY_ENDPOINT= f"{RESOURSE_URL}api/v1/events/{eventId}/history"

        with allure.step("Получение заголовков авторизации для инженера"):
            response1 = auth_api.auth_headers(data_engineer_preprod)

        with allure.step("Отправка запроса USERS_ME_ENDPOINT"):
            response2 = requests.get(USERS_ME_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response2,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса EVENTS_ENDPOINT"):
            response3 = requests.get(EVENTS_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response3,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса EVENTS_ID_ENDPOINT"):
            EVENTS_ID_ENDPOINT = f"{RESOURSE_URL}api/v1/events/{eventId}/"
            response4 = requests.get(EVENTS_ID_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response4,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса RISKS_ENDPOINT"):
            response5 = requests.get(RISKS_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response5,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"

        with allure.step("Отправка запроса CATEGORIES_ENDPOINT"):
            response7 = requests.get(CATEGORIES_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response7,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса TASKS_ENDPOINT"):
            response8 = requests.get(TASKS_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response8,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса EVENTS_STATUS_RU_ENDPOINT"):
            response9 = requests.get(EVENTS_STATUS_RU_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response9,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса EVENTS_STATUS_EN_ENDPOINT"):
            response10 = requests.get(EVENTS_STATUS_EN_ENDPOINT, headers=response1)
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
        with allure.step("Отправка запроса SEASONS_MINE_ENDPOINT"):
            response13 = requests.get(SEASONS_MINE_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response13,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса PLACES_MINE_ENDPOINT"):
            response14 = requests.get(PLACES_MINE_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response14,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса EVENTS_ID_HISTORY_ENDPOINT"):
            response15 = requests.get(EVENTS_ID_HISTORY_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response15,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса RISKS_ID_ENDPOINT"):
            response16 = requests.get(RISKS_ID_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response16,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса RISKS_ID_EVENT_ENDPOINT"):
            response18 = requests.get(RISKS_ID_EVENT_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response18,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"

        with allure.step("Отправка PUT запроса EVENTS_ID_ENDPOINT"):
            response19 = requests.put(EVENTS_ID_ENDPOINT, headers=response1, json=EVENT_DATA_SET)
            Assertions.assert_code_status(response19,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка PATCH запроса EVENTS_ID_ENDPOINT"):
            response20 = requests.patch(EVENTS_ID_ENDPOINT, headers=response1, json=EVENT_DATA_GET)
            Assertions.assert_code_status(response20,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
        with allure.step("Отправка запроса USER_ENDPOINT"):
            response21 = requests.get(USER_ENDPOINT, headers=response1)
            Assertions.assert_code_status(response21,
                                      200), "Ожидался статус {expected_status}, но получен {response.status_code}\n"
