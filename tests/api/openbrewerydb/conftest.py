import copy
import random

import pytest
from src.api.simple_api_client import SimpleApiClient
from tests.api.openbrewerydb.test_openbrewerydb_pydantic import Brewery

proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080"
}

base_url = 'https://api.openbrewerydb.org/breweries'

CHOICES = 3


@pytest.fixture(scope='session')
def api():
    yield SimpleApiClient(url=base_url, verify=False, proxies=proxies)


def breweries():
    with SimpleApiClient(url=base_url, verify=False, proxies=None).GET('/search?query=*') as r:
        for j in r.json():
            yield j


raw = {k: set() for k in Brewery.__fields__.keys()}
xfailed = copy.deepcopy(raw)

# API recognizes 'proprieter' but a lot of records consist 'proprietor' instead
# API do not recognize brewery_type = 'taproom' but some of items consist it (England)

for b in breweries():
    for k, v in b.items():
        raw[k].add(v)
        if (b['brewery_type'] in ('taproom',)):
            xfailed[k].add(v)

random_choises = {k: random.sample(raw[k], CHOICES) for k in (
    'id', 'name', 'city', 'country', 'state', 'postal_code')}


def params_filter(p_name):
    def wrapper(p):
        if p in xfailed[p_name]:
            return pytest.param(p, marks=pytest.mark.xfail(strict=True))
        return p
    return wrapper


@ pytest.fixture(params=map(params_filter('id'), random_choises['id']), scope='session')
def brewery_id(request):
    yield request.param


@ pytest.fixture(params=map(params_filter('name'), random_choises['name']), scope='session')
def brewery_name(request):
    yield request.param


@ pytest.fixture(params=(b for b in raw['brewery_type']), scope='session')
def brewery_type(request):
    yield request.param


@ pytest.fixture(params=map(params_filter('city'), random_choises['city']), scope='session')
def city(request):
    yield request.param


@ pytest.fixture(params=map(params_filter('state'), random_choises['state']), scope='session')
def state(request):
    yield request.param


@ pytest.fixture(params=map(params_filter('country'), random_choises['country']), scope='session')
def country(request):
    yield request.param


@ pytest.fixture(params=map(params_filter('postal_code'), random_choises['postal_code']), scope='session')
def postal_code(request):
    yield request.param


if __name__ == '__main__':
    pass
