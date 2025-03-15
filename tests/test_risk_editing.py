import uuid
import allure
import pytest

from src.api.categories_api import get_categories_mine
from src.api.event_api import create_event_by_risk_id, patch_event_by_id
from src.api.places_api import get_places_mine
from src.api.risk_api import create_risk, get_risk_by_id, patch_risk_by_id
from src.api.users_api import get_users
from src.test_data.events_data import EVENT_DATA, EVENT_DATA_CLOSED, EVENT_DATA_APPROVED
from src.test_data.risks_data import RISK_DATA_CLOSED, RISK_DATA_WORK, RISK_DATA_APPROVED, RISK_DATA_DEVATION
from src.test_data.users_data import DATA_HUNTER, DATA_RM_PREPROD
from src.utils.assertions import Assertions


@allure.title("Статусая схема риска ")
@allure.description("Тестирование проверки статусной схемы риска через API")
@pytest.mark.smoke
def test_create_risk(create_headers_for_test):
    with allure.step("Получение списка территорий"):
        print("Получение списка территорий")
        get_places = get_places_mine(by_user=DATA_RM_PREPROD)
        Assertions.assert_code_status(get_places, 200)
        places = get_places.json()
        if places:
            place_id = places[0].get('id')
        else:
            print("Список мест пуст.")
        print(place_id)

    with allure.step("Получение списка категорий"):
        print("Получение списка категорий")
        get_categories = get_categories_mine(by_user=DATA_RM_PREPROD)
        Assertions.assert_code_status(get_categories, 200)
        categories = get_categories.json()
        if 'items' in categories and categories['items']:
            cat_id = categories['items'][0].get('id')
            print(f"ID первой категории: {cat_id}")
        else:
            print("Список категорий пуст.")
        print(cat_id)

    with allure.step("Получение списка пользователей"):
        print("Получение списка пользователей")
        get_user = get_users(by_user=DATA_RM_PREPROD)
        Assertions.assert_code_status(get_user, 200)
        users = get_user.json()
        if 'items' in users and users['items']:
            user_id = users['items'][0].get('id')
        else:
            print("Список пользователей пуст.")
        print(user_id)

    with allure.step("Создание нового риска"):
        print("Создание нового риска")

        RISK_DATA_NOW = {
            "uniqueId": str(uuid.uuid4()),
            "description": "Создание риска через автотест",
            "category": {'id': cat_id},
            "place": {"id": place_id},
            "priority": {"id": -1},
            "user": {"id": user_id},
            "status": {"id": 1}
        }
        created_risk = create_risk(by_user=DATA_HUNTER, risk_data=RISK_DATA_NOW)
        Assertions.assert_code_status(created_risk, 200)
        Assertions.assert_json_has_key(created_risk, ["id"])
        risk_id = created_risk.json().get('id')
        print(f"Создан риск с номером: {risk_id}")

    with allure.step("Получение информации по созданному риску"):
        print("Получение информации по созданному риску")
        get_risk = get_risk_by_id(by_user=DATA_HUNTER, risk_id=risk_id)
        Assertions.assert_code_status(get_risk, 200)

    with allure.step("Отклоняем риск из статуса новый"):
        print("Отклоняем риск из статуса новый")

        deviation_risk = patch_risk_by_id(by_user=DATA_RM_PREPROD, risk_id=risk_id, risk_data=RISK_DATA_DEVATION)

        print(deviation_risk)
        Assertions.assert_code_status(deviation_risk, 200)
        Assertions.assert_json_has_key(deviation_risk, ["id"])
        print(f"Отклонен риск {risk_id}")

    with allure.step("Принимаем риск и присваиваем приоритет"):
        print("Принимаем риск и присваиваем приоритет")

        approved_risk = patch_risk_by_id(by_user=DATA_RM_PREPROD, risk_id=risk_id, risk_data=RISK_DATA_APPROVED)
        Assertions.assert_code_status(approved_risk, 200)
        Assertions.assert_json_has_key(approved_risk, ["id"])
        print(approved_risk.text)

    with allure.step("Отклоняем риск из статуса принят"):
        print("Отклоняем риск из статуса принят")

        deviation_risk = patch_risk_by_id(by_user=DATA_RM_PREPROD, risk_id=risk_id, risk_data=RISK_DATA_DEVATION)
        Assertions.assert_code_status(deviation_risk, 200)
        Assertions.assert_json_has_key(deviation_risk, ["id"])
        print(f"Отклонен риск {risk_id}")

    with allure.step("Принимаем риск и присваиваем приоритет"):
        print("Принимаем риск и присваиваем приоритет")

        approved_risk = patch_risk_by_id(by_user=DATA_RM_PREPROD, risk_id=risk_id, risk_data=RISK_DATA_APPROVED)
        Assertions.assert_code_status(approved_risk, 200)
        Assertions.assert_json_has_key(approved_risk, ["id"])
        print(approved_risk.text)

    with allure.step("Создаем мероприятие для риска"):
        print("Создаем мероприятие для риска")

        created_event = create_event_by_risk_id(by_user=DATA_RM_PREPROD, risk_id=risk_id, event_data=EVENT_DATA)
        event_id = created_event.json().get('id')
        Assertions.assert_code_status(created_event, 200)
        Assertions.assert_json_has_key(created_event, ["id"])
        print(created_event.text)

    with allure.step("Переводим риск в статус: 'В работе'"):
        print("Переводим риск в статус: 'В работе'")

        work_risk = patch_risk_by_id(by_user=DATA_RM_PREPROD, risk_id=risk_id, risk_data=RISK_DATA_WORK)
        Assertions.assert_code_status(work_risk, 200)
        Assertions.assert_json_has_key(work_risk, ["id"])
        print(work_risk.text)

    with allure.step("Принимаем мероприятие"):
        print("Принимаем мероприятие")

        approved_event = patch_event_by_id(by_user=DATA_RM_PREPROD, event_id=event_id, event_data=EVENT_DATA_APPROVED)
        Assertions.assert_code_status(approved_event, 200)
        Assertions.assert_json_has_key(approved_event, ["id"])
        print(approved_event.text)

    with allure.step("Закрываем мероприятие"):
        print("Закрываем мероприятие")

        closed_event = patch_event_by_id(by_user=DATA_RM_PREPROD, event_id=event_id, event_data=EVENT_DATA_CLOSED)
        Assertions.assert_code_status(closed_event, 200)
        Assertions.assert_json_has_key(closed_event, ["id"])
        print(closed_event.text)

    with allure.step("Закрываем риск"):
        print("Закрываем риск")

        closed_risk = patch_risk_by_id(by_user=DATA_RM_PREPROD, risk_id=risk_id, risk_data=RISK_DATA_CLOSED)
        Assertions.assert_code_status(closed_risk, 200)
        Assertions.assert_json_has_key(closed_risk, ["id"])
        print(closed_risk.text)
