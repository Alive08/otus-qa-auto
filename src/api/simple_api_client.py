from socket import timeout
import requests
import json


proxies = {
    "http": "http://vkozlov:8080",
    "https": "http://vkozlov:8080"
}


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
        return self.session.get(self.url + url, **kwargs)

    def POST(self, url='', **kwargs):
        return self.session.post(self.url + url, **kwargs)



c = SimpleApiClient(proxies=proxies, verify=False, timeout=1)
c.url = 'https://dog.ceo/api/'
r = c.GET('breeds/list')

print(r.status_code)

