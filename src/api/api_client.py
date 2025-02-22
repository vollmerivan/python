from requests import Request, Session, Response
from functools import lru_cache
from src.config.endpoints import AUTH_ENDPOINT, Admin_AUTH_ENDPOINT
from src.config.settings import host
from src.test_data.users_data import UsersData, SUPER_USER


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
        token = session.post(host+login_url, headers=None, json=payload).json().get('token')
        session.headers['Authorization'] = f'Braer {token}'

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
        print(response)
        return response

api_client = Client(host=host)
