import pytest
import allure
import src.test_data.users_data
from src.config.endpoints import AUTH_ENDPOINT
from src.utils.assertions import Assertions


@pytest.mark.parametrize("user_data, expected_status, description", [
    (src.test_data.users_data.data_rm_preprod, 200, "Позитивный сценарий с корректными данными"),
    (src.test_data.users_data.invalid_pass, 401, "Негативный сценарий с некорректным паролем"),
    (src.test_data.users_data.invalid_empty_login, 400, "Негативный сценарий с пустым логином"),
    (src.test_data.users_data.invalid_empty_pass, 400, "Негативный сценарий с пустым паролем"),
    (src.test_data.users_data.invalid_empty, 400, "Негативный сценарий с пустыми логином и паролем"),
    (src.test_data.users_data.invalid_login_pass, 401, "Негативный сценарий с некорректным логином и паролем"),
    (src.test_data.users_data.invalid_login, 401, "Негативный сценарий с некорректным логином")
])
@allure.epic("Тестирование API авторизации")
@allure.feature("Логин пользователя")
def test_user_login(create_headers_for_test, user_data, expected_status, description):
    """
    Тестирование авторизации пользователя с валидными и не валидными данными.
    """
    allure.dynamic.story(description)
    allure.dynamic.severity(
        allure.severity_level.BLOCKER if expected_status == 200 else allure.severity_level.CRITICAL
    )
    allure.dynamic.title(f"Тест авторизации: {description}")

    with allure.step("Отправка запроса на логин"):
        auth_header = create_headers_for_test(url=AUTH_ENDPOINT, payload=user_data)

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
