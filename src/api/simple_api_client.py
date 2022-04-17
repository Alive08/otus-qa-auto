import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class SimpleApiClient:

    def __init__(self, url='', **kwargs) -> None:

        self.session = requests.Session()

        for k, v in kwargs.items():
            self.__dict__[k] = v
            self.session.__dict__[k] = v

        self.url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    def GET(self, url='', **kwargs):
        self.response = self.session.get(self.url + url, **kwargs)
        return self.response

    def POST(self, url='', **kwargs):
        self.response = self.session.post(self.url + url, **kwargs)
        return self.response

    def check_if_success(self):
        res = True
        if hasattr(self, 'validator'):
            res = self.validator(self)
        return res and self.response.status_code == 200

