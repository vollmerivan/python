import pytest
import allure

from src.api.auth_api import auth
from src.test_data.users_data import DATA_RM_PREPROD, INVALID_PASS, INVALID_EMPTY_LOGIN, INVALID_EMPTY_PASS, \
    INVALID_EMPTY, INVALID_LOGIN_PASS, INVALID_LOGIN
from src.utils.assertions import Assertions


@pytest.mark.parametrize("user_data, expected_status, description", [
    (DATA_RM_PREPROD, 200, "Позитивный сценарий с корректными данными"),
    (INVALID_PASS, 401, "Негативный сценарий с некорректным паролем"),
    (INVALID_EMPTY_LOGIN, 400, "Негативный сценарий с пустым логином"),
    (INVALID_EMPTY_PASS, 400, "Негативный сценарий с пустым паролем"),
    (INVALID_EMPTY, 400, "Негативный сценарий с пустыми логином и паролем"),
    (INVALID_LOGIN_PASS, 401, "Негативный сценарий с некорректным логином и паролем"),
    (INVALID_LOGIN, 401, "Негативный сценарий с некорректным логином")
])
@allure.epic("Тестирование API авторизации")
@allure.feature("Логин пользователя")
def test_user_login(user_data, expected_status, description):

    allure.dynamic.story(description)
    allure.dynamic.severity(
        allure.severity_level.BLOCKER if expected_status == 200 else allure.severity_level.CRITICAL
    )
    allure.dynamic.title(f"Тест авторизации: {description}")

    with allure.step("Отправка запроса на логин"):
        auth_header = auth(by_user=user_data)

    with allure.step("Проверка статуса ответа"):
        Assertions.assert_code_status(auth_header, expected_status)

        with allure.step("Анализ содержимого ответа"):
            response_data = auth_header.json()
            if expected_status == 200:
                allure.attach(
                    "Авторизация успешна!",
                    name="Сообщение",
                    attachment_type=allure.attachment_type.TEXT
                )
                assert "token" in response_data, "Токен отсутствует в ответе"
                assert response_data["token"], "Токен пустой"
            elif expected_status == 401:
                allure.attach(
                    "Неверный логин или пароль.",
                    name="Сообщение",
                    attachment_type=allure.attachment_type.TEXT
                )
                assert "error" in response_data, "Сообщение об ошибке отсутствует в ответе"
                assert response_data["error"], "Сообщение об ошибке пустое"
