import io

import requests
from requests import Request, Session, Response
from functools import lru_cache
from src.config.endpoints import AUTH_ENDPOINT, Admin_AUTH_ENDPOINT
from src.config.settings import host
from src.test_data.users_data import UsersData, SUPER_USER
from src.utils import log

_request_logging_curl_template = """
Request:
{curl}
"""

_response_logging_template_ = """
Response:
/tstatus-code: {status} {reason}
/telapsed: {elapsed}
/tresponse_headers: {response_headers}
/tbody: {response_body}
"""


class Client:

    def __init__(self, host: str) -> None:
        self.host = host

    @lru_cache()
    def user_session(self, by_user: UsersData | None = None) -> Session:
        session = Session()
        payload = {
            'email': by_user.email,
            'password': by_user.password
        }
        login_url = Admin_AUTH_ENDPOINT if by_user == SUPER_USER else AUTH_ENDPOINT
        token = session.post(host + login_url, headers=None, json=payload).json().get('token')
        session.headers['Authorization'] = f'Bearer {token}'

        return session

    def _set_request_url(self, request: Request) -> None:
        request.url = self.host + request.url

    def send_request(
            self,
            request: Request,
            by_user: UsersData,
            session: Session | None = None
    ) -> Response:
        if session is None:
            session = self.user_session(by_user=by_user)

        self._set_request_url(request)

        prepared_request = session.prepare_request(request)

        response = session.send(prepared_request)

        curl = _api_call_to_curl(request=prepared_request, is_file=False, response=response)

        log.info(curl)

        return response


def _text_body_to_json(text: str, json_lib=None) -> str:
    """Default fallback if we have in request.body not file or string of bytes

    :param text: request.body text
    """
    try:
        text = json_lib.loads(text)
        return json_lib.dumps(text, ensure_ascii=False, indent=4)
    except Exception:
        return text


_response_logging_template = (
    "Response:\n"
    "  Elapsed: {elapsed}\n"
    "  Status: {status}\n"
    "  Reason: {reason}\n"
    "  Headers:\n\t\t{response_headers}\n"
    "  Body: {response_body}\n"
)


def _api_call_to_curl(
        request: requests.PreparedRequest,
        is_file: bool = False,
        response: requests.Response = None,
        _response_logging_template=_response_logging_template) -> str:
    """
    Format request and response to CURL

    :param request: request as PreparedRequest type
    :param cookies: request cookies
    :param is_file: bool to check if we send a file
    :param response: response as requests.Response
    """
    headers = ' \\\n  -H '.join([f'"{k}: {v}"' for k, v in request.headers.items()])
    body = None
    if isinstance(request.body, io.BufferedReader) or is_file:
        body = 'Binary File'
    elif isinstance(request.body, bytes) and request.body:
        body = request.body.decode('utf-8')
    elif request.body is not None:
        body = _text_body_to_json(request.body)

    curl_body_parameter = '' if body is None else f" -d '{body}' \\\n "
    curl = (f'curl --compressed -v -X {request.method} \\\n  -H {headers}'
            f"\\\n {curl_body_parameter} '{request.url}'")
    log_stdout = _request_logging_curl_template.format(curl=curl)
    if response is not None:
        response_body = _text_body_to_json(response.text)
        headers_delimiter = '\n\t\t'
        response_body = _response_logging_template.format(
            elapsed=response.elapsed,
            status=response.status_code,
            reason=response.reason,
            response_headers=headers_delimiter.join([f'{key}: {value}' for key, value in response.headers.items()]),
            response_body=response_body,
        )
        log_stdout += '\n' + response_body
    return log_stdout


api_client = Client(host=host)
