import os

host = "https://hunter-dev.krit.pro/"


class ApiLogConfig:
    CONSOLE: bool = os.getenv(key='LOG_CONSOLE', default=None)
    FILE: bool = os.getenv(key='LOG_FILE', default=None)


api_log_config = ApiLogConfig()
