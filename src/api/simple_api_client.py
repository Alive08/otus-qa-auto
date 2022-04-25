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

    def get_all_pages(self, url='', **kwargs):
        params = {}
        if 'params' in kwargs:
            params.update(kwargs['params'])
            try:
                per_page = params['per_page']
            except:
                params.update({'per_page': 50})
        page = 0
        buf = []
        while True:
            params.update({'page': page})
            r = self.GET(url, params=params)
            assert r.ok
            buf.extend(r.json())
            if len(r.json()) < params['per_page']:
                break
            page += 1
        return buf

    def check_if_success(self):
        res = True
        if hasattr(self, 'validator'):
            res = self.validator(self)
        return res and self.response.status_code == 200
