import pytest
import allure

from src.api.event_api import create_event_by_risk_id, get_event_history_by_id, get_event_by_id, put_event_by_id, \
    patch_event_by_id
from src.api.users_api import post_roles_by_user, get_any, get_users
from src.test_data.users_data import DATA_ADMIN_PREPROD, DATA_RM_PREPROD, DATA_ENGINEER_PREPROD, role_engineer
from src.config.endpoints import (
    RISKS_ENDPOINT, USERS_ME_ENDPOINT, USER_ENDPOINT, PLACES_MINE_ENDPOINT, CATEGORIES_ENDPOINT,
    TASKS_ENDPOINT, RISKS_STATUS_EN_ENDPOINT, RISKS_STATUS_RU_ENDPOINT, EVENTS_STATUS_RU_ENDPOINT,
    EVENTS_STATUS_EN_ENDPOINT,
    SEASONS_MINE_ENDPOINT, EVENTS_ENDPOINT,
    RISKS_ID_EVENT_ENDPOINT, RISKS_ID_ENDPOINT)
from src.utils.assertions import Assertions
from src.test_data.events_data import EVENT_DATA_GET, EVENT_DATA_SET, EVENT_DATA



@allure.title("Тест на создание роли инженера")
@allure.description("Проверка успешного присвоения роли инженера и получения списка ролей")
def test_post_engineer_role():
        with (allure.step("Присвоения роли инженера")):

            post_engineer_role = post_roles_by_user(by_user=DATA_ADMIN_PREPROD, user_id=178, role_id=role_engineer)  # 70/178 айди поьзователя из препрод/dev
            assert post_engineer_role.status_code in (200, 409), f"Ожидалось 200 или 409, но получен: {post_engineer_role.status_code}"


@allure.title("Тест на создание мероприятия")
@allure.description("Проверка успешного создания мероприятия и запись его ИД в переменную")
@pytest.fixture
def test_post_event():
        post_event = create_event_by_risk_id(by_user=DATA_RM_PREPROD, risk_id=572, event_data=EVENT_DATA)  #  194 препрод, 572 дев
        Assertions.assert_code_status(post_event,200)

        event_id = post_event.json().get('id')
        return event_id


@allure.title("Тест на получение данных инженера")
@allure.description("Проверка доступности различных API для пользователя-инженера")
def test_get_engineer(test_post_event):
    event_id = test_post_event

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
            get_response = get_any(url=endpoint, by_user=DATA_ENGINEER_PREPROD)
            Assertions.assert_code_status(get_response, 200)


    with allure.step("Отправка запроса EVENTS_ID_ENDPOINT"):
        get_event = get_event_by_id(by_user=DATA_RM_PREPROD, event_id=event_id)
        Assertions.assert_code_status(get_event, 200)


    with allure.step("Отправка запроса EVENTS_ID_HISTORY_ENDPOINT"):
        get_event_history = get_event_history_by_id(by_user=DATA_RM_PREPROD, event_id=event_id)
        Assertions.assert_code_status(get_event_history, 200)

    with allure.step("Отправка PUT запроса EVENTS_ID_ENDPOINT"):
        put_event = put_event_by_id(by_user=DATA_RM_PREPROD, event_id=event_id, event_data=EVENT_DATA_SET)
        Assertions.assert_code_status(put_event, 200)

    with allure.step("Отправка PATCH запроса EVENTS_ID_ENDPOINT"):
        patch_event = patch_event_by_id(by_user=DATA_RM_PREPROD, event_id=event_id, event_data=EVENT_DATA_GET)
        Assertions.assert_code_status(patch_event, 200)

    with allure.step("Отправка запроса USER_ENDPOINT"):
        users_get = get_users(by_user=DATA_RM_PREPROD)
        Assertions.assert_code_status(users_get, 200)
