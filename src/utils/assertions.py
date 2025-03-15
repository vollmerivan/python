import json
from requests import Response


class Assertions:


    """Метод для проверки статус кода"""

    @staticmethod
    def assert_code_status(response: Response, expected_status):

        if response.status_code == expected_status:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print(
                f"Ожидался статус {expected_status}, но получен {response.status_code}\n"
                f"Тело ответа: {response.text}\n"
                f"Тело запроса: {response.request.body}"
            )
        assert response.status_code == expected_status



    """Метод проверки ответа на формат JSON"""

    @staticmethod
    def assert_json_token(response: Response, name: str):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в формате JSON. Текст ответа '{response.text}'"

        assert name in response_as_dict, (
            f"В ответе JSON нет ключа '{name}'.\n"
            f"Тело запроса: {response.request.body}\n"
            f"Статус-код: {response.status_code}\n"
            f"Тело ответа: {response.text}\n"
        )



    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def assert_json_has_key(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print(f"Поля {expected_value} присутствуют")



    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def assert_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен !!!")


    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""
    @staticmethod
    def assert_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f"Текст:   {search_word} - присутствует !!!")
        else:
            print(f"Текст:   {search_word} - отсутствует !!!")
