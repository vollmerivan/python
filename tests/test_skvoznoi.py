import pytest
import random
import allure
import uuid
from datetime import datetime

from src.api.categories_api import create_categories
from src.api.org_admin_api import create_organization
from src.api.places_api import create_places
from src.api.risk_api import create_risk, get_risks
from src.api.users_api import create_user_admin, patch_user_admin, post_roles_by_user_admin
from src.test_data.users_data import password_data, role_admin_data, role_rm_data, SUPER_USER

from src.utils.assertions import Assertions
from src.test_data.org_data import org_data




@allure.title("Сквозной тест")
@allure.description("Тестирование создания организации, пользоватея, справочников и риска ")
@pytest.fixture
def test_post_org(create_headers_for_test):
    with allure.step("Создание организации"):
        create_org = create_organization(by_user=SUPER_USER, org_data=org_data)
        Assertions.assert_code_status(create_org, 200)
        org_id = create_org.json().get('id')
        print(f"Создана организация с name: {org_data['name']} и id: {org_id}")

    with allure.step("Создание пользователя в организации"):
        user_data = {
            "name": f"User{random.randint(1, 999)}",
            "email": f"user{datetime.now().strftime('%m%d%y%H%M')}@krit.pro",
            "isActive": True,
            "organization": {"id": org_id}
        }
        create_user = create_user_admin(by_user=SUPER_USER, user_data=user_data)
        Assertions.assert_code_status(create_user, 200)
        user_id = create_user.json().get('id')
        print(f"Создан пользователь с email: {user_data['email']} и id: {user_id}")
        user_email = user_data['email']

    with allure.step("Присвоение пароля созданному пользователю"):
        set_pass_user = patch_user_admin(by_user=SUPER_USER, user_id=user_id, patch_data=password_data)
        Assertions.assert_code_status(set_pass_user, 200)
        print(f'Пароль присвоен {password_data['password']} для пользователя {user_id}')


    with allure.step("Присвоение роли администратор пользователю"):
        set_role_admin_user = post_roles_by_user_admin(by_user=SUPER_USER, user_id=user_id, role_id=role_admin_data)
        Assertions.assert_code_status(set_role_admin_user, 200)
        print(f'Присвоена роль администратора для пользователя {user_id}')


    with allure.step("Присвоение роли риск-менеджер пользователю"):
        set_role_rm_user = post_roles_by_user_admin(by_user=SUPER_USER, user_id=user_id, role_id=role_rm_data)
        Assertions.assert_code_status(set_role_rm_user, 200)
        print(f'Присвоена роль риск-менеджер для пользователя {user_id}')

        return user_email, user_id, org_id


@pytest.fixture
def test_post_directory(create_headers_for_test, test_post_org):
    user_email, user_id, org_id = test_post_org
    data_user: dict = {"email": user_email, "password": "super"}


    with (allure.step("Создание новой категории")):
        create_new_category = create_categories(by_user=data_user)
        Assertions.assert_code_status(create_new_category, 200)
        Assertions.assert_json_has_key(create_new_category, "id")
        cat_id = create_new_category.json().get("id")
        print(f"Создана категория {cat_id}")

    with (allure.step("Создание новой территории")):
        create_new_place = create_places(by_user=data_user)
        Assertions.assert_code_status(create_new_place, 200)
        Assertions.assert_json_has_key(create_new_place, "id")
        place_id = create_new_place.json().get("id")
        print(f"Создана территория {place_id}")

        return user_email, cat_id, place_id, user_id


@allure.title("Создание риска")
@allure.description("Тестирование создания нового риска через API")
def test_create_risk(create_headers_for_test, test_post_directory):
    user_email, cat_id, place_id, user_id = test_post_directory

    data_user = {'email': user_email, 'password': 'super'}

    with (allure.step("Создание нового риска")):
        risk_data_now = {
            "uniqueId": str(uuid.uuid4()),
            "description": "Создание риска через автотест 'skvoznoi'",
            "category": {'id': cat_id},
            "place": {"id": place_id},
            "priority": {"id": -1},
            "user": {"id": user_id},
            "status": {"id": 1}
        }
        response2 = create_risk(by_user=data_user, risk_data=risk_data_now)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        print(f"Создан риск {response2.json().get("id")}")

    with (allure.step("Получение списка рисков")):
        get_risk = get_risks(by_user=data_user)
        Assertions.assert_code_status(get_risk, 200)
