import json
from requests import Response

class Assertions:
    @staticmethod
    def assert_json_has_key(response: Response, name):
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

    @staticmethod
    def assert_code_status(response: Response, expected_status):
        assert response.status_code == expected_status, (
            f"Ожидался статус {expected_status}, но получен {response.status_code}\n"
            f"Тело ответа: {response.text}\n"
            f"Тело запроса: {response.request.body}"
        )