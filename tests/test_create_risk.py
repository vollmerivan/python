import allure
import pytest

from src.api.risk_api import create_risk, get_risk_by_id, delete_risk_by_id
from src.test_data.users_data import DATA_HUNTER
from src.utils.assertions import Assertions


 
@allure.title("Создание и удаление риска ")
@allure.description("Тестирование создания и удаления нового риска через API")
@pytest.mark.smoke
def test_create_risk():
    with allure.step("Создание нового риска"):
        created_risk = create_risk(by_user=DATA_HUNTER)
        Assertions.assert_code_status(created_risk, 200)
        Assertions.assert_json_has_key(created_risk, ["id"])
        risk_id = created_risk.json().get('id')


    with allure.step("Получение информации по созданному риску"):
        get_risk = get_risk_by_id(by_user=DATA_HUNTER, risk_id=risk_id)
        Assertions.assert_code_status(get_risk, 200)
        # Assertions.assert_json_has_key(get_risk, ["id", 'author', "description", "place", "category", "status"])
        # не могу понять как валидировать значения в списке


    with allure.step("Удаление риска"):
        delete_risk = delete_risk_by_id(by_user=DATA_HUNTER, risk_id=risk_id)
        Assertions.assert_code_status(delete_risk, 200)

    with allure.step("Проверка удаления риска"):
        get_delete_risk = get_risk_by_id(by_user=DATA_HUNTER, risk_id=risk_id)
        Assertions.assert_code_status(get_delete_risk, 404)
        Assertions.assert_json_search_word_in_value(get_delete_risk, "error", "Not Found")
