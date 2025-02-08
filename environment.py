import os


class Environment:
    DEV = 'dev'
    PREPROD = 'preprod'

    URLS = {
        DEV: "https://hunter-dev.krit.pro/",
        PREPROD: "https://hunter-preprod.krit.pro/"
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value ENV variable {self.env}")

ENV_OBJECT = Environment()
