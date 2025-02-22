import pytest
import random
import allure
import uuid
from datetime import datetime
from src.test_data.users_data import superuser, password_data, role_admin_data, role_rm_data
from src.config.endpoints import Admin_ORG_ENDPOINT, Admin_USER_ENDPOINT, CATEGORIES_ENDPOINT, PLACES_ENDPOINT, \
    RISKS_ENDPOINT, Admin_AUTH_ENDPOINT, AUTH_ENDPOINT
from src.utils.assertions import Assertions
from src.test_data.org_data import org_data
from src.test_data.other_data import category_data, place_data
from src.utils.api_client_fast import Myrequests
from tests.conftest import create_headers_for_test


@allure.title("Сквозной тест")
@allure.description("Тестирование создания организации, пользоватея, справочников и риска ")
@pytest.fixture
def test_post_org(create_headers_for_test):
    with allure.step("Получение заголовков авторизации"):
        auth_header = create_headers_for_test(url=Admin_AUTH_ENDPOINT, payload=superuser)
    with allure.step("Создание организации"):
        response2 = Myrequests.post(Admin_ORG_ENDPOINT, headers=auth_header, json=org_data)
        Assertions.assert_code_status(response2, 200)
        org_id = response2.json().get('id')
        print(f"Создана организация с name: {org_data['name']} и id: {org_id}")

    with allure.step("Создание пользователя в организации"):
        user_data = {
            "name": f"User{random.randint(1, 999)}",
            "email": f"user{datetime.now().strftime('%m%d%y%H%M')}@krit.pro",
            "isActive": True,
            "organization": {"id": org_id}
        }
        response3 = Myrequests.post(Admin_USER_ENDPOINT, headers=auth_header, json=user_data)
        Assertions.assert_code_status(response3, 200)
        user_id = response3.json().get('id')
        print(f"Создан пользователь с email: {user_data['email']} и id: {user_id}")
        user_email = user_data['email']

    with allure.step("Присвоение пароля созданному пользователю"):
        Admin_USER_patch_ENDPOINT = f"{ADMIN_URL}api/v1/users/{user_id}"
        response4 = Myrequests.patch(Admin_USER_patch_ENDPOINT, headers=auth_header, json=password_data)
        Assertions.assert_code_status(response4, 200)
        print(f'Пароль присвоен {password_data['password']} для пользователя {user_id}')
    with allure.step("Присвоение пароля созданному пользователю"):
        Admin_role_ENDPOINT = f"{ADMIN_URL}api/v1/users/{user_id}/roles"
    with allure.step("Присвоение роли администратор пользователю"):
        response5 = Myrequests.post(Admin_role_ENDPOINT, headers=auth_header, json=role_admin_data)
        Assertions.assert_code_status(response5, 200)
        print(f'Присвоена роль администратора для пользователя {user_id}')
    with allure.step("Присвоение роли риск-менеджер пользователю"):
        response6 = Myrequests.post(Admin_role_ENDPOINT, headers=auth_header, json=role_rm_data)
        Assertions.assert_code_status(response6, 200)
        print(f'Присвоена роль риск-менеджер для пользователя {user_id}')

        return user_email, user_id, org_id


@pytest.fixture
def test_post_directory(create_headers_for_test, test_post_org):
    user_email, user_id, org_id = test_post_org
    with allure.step("Получение заголовков авторизации созданного пользователя"):
        data_user = {"email": user_email, "password": "super"}
        auth_header = create_headers_for_test(url=AUTH_ENDPOINT, payload=data_user)

    with (allure.step("Создание новой категории")):
        response2 = Myrequests.post(CATEGORIES_ENDPOINT, headers=auth_header, json=category_data)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        cat_id = response2.json().get("id")
        print(f"Создана категория {cat_id}")

    with (allure.step("Создание новой территории")):
        response3 = Myrequests.post(PLACES_ENDPOINT, headers=auth_header, json=place_data)
        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "id")
        place_id = response3.json().get("id")
        print(f"Создана территория {place_id}")

        return user_email, cat_id, place_id, user_id


@allure.title("Создание риска")
@allure.description("Тестирование создания нового риска через API")
def test_create_risk(create_headers_for_test, test_post_directory):
    user_email, cat_id, place_id, user_id = test_post_directory
    with allure.step("Получение заголовков авторизации"):
        data_user = {'email': user_email, 'password': 'super'}
        auth_header = create_headers_for_test(url=AUTH_ENDPOINT, payload=data_user)

    with (allure.step("Создание нового риска")):
        RISK_DATA = {
            "uniqueId": str(uuid.uuid4()),
            "description": f"Создание риска через автотест 'skvoznoi'",
            "category": {'id': cat_id},
            "place": {"id": place_id},
            "priority": {"id": -1},
            "user": {"id": user_id},
            "status": {"id": 1}
        }
        response2 = Myrequests.post(RISKS_ENDPOINT, headers=auth_header, json=RISK_DATA)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        print(f"Создан риск {response2.json().get("id")}")

    with (allure.step("Получение списка рисков")):
        response3 = Myrequests.get(RISKS_ENDPOINT, headers=auth_header)
        Assertions.assert_code_status(response3, 200)
