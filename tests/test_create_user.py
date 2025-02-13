"""Попытка написать тест на создание пользователя,. с помощью двух фикстур"""

from src.test_data.users_data import data_admin_preprod
def test_create_user(create_user):
    response = create_user(data_admin_preprod)
    print(response)

