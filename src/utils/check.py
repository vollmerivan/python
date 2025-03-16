
from requests import Response

from src.utils import asserts


def check_code_status(response: Response, status_code: int) -> None:
    actual_status_code = response.status_code
    error_massege = f"Expected: '{status_code}'\n" f"Actual: '{actual_status_code}'\n"
    asserts.equal(response.status_code, actual_status_code, error_massege)


def check_response(response: Response, status_code: int=200) -> dict:
    check_code_status(response, status_code)
    return response.json()