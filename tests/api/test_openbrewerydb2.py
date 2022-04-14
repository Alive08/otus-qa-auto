from types import NoneType
import pytest
from requests import request
from typing import List, Dict
from src.api.simple_api_client import SimpleApiClient
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from pydantic import BaseModel, HttpUrl, NoneStr, ValidationError, conlist


base_url = 'https://api.openbrewerydb.org/breweries'


proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080"
}


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    street: str = None
    address_2: str = None
    address_3: str = None
    city: str
    state: str
    county_province: str = None
    postal_code: str
    country: str
    longitude: str = None
    latitude: str = None
    phone: str = None
    website_url: HttpUrl = None
    updated_at: str
    created_at: str


class NonEmptyBreweryList(BaseModel):
    l: conlist(item_type=Brewery, min_items=1)


class BreweryList(BaseModel):
    l: list[Brewery]


@pytest.fixture(scope='session')
def api():

    yield SimpleApiClient(url=base_url, verify=False, proxies=None)


def breweries():
    with SimpleApiClient(url=base_url, verify=False, proxies=None).GET('/') as r:
        for j in r.json():

            yield j


@pytest.fixture(params=breweries(), ids=lambda v: v['name'], scope='session')
def brewery_list(request):
    yield request.param


def test_brewery_list_all(brewery_list):
    try:
        Brewery(**brewery_list)
    except ValidationError as e:
        print(e.json())
        pytest.fail()


def test_brewery_search(api):
    r = api.GET('/search', params={'query': 'brewfarm'})
    assert api.check_if_success()
    print(r.json())
    try:
        BreweryList(**{'l': r.json()})
    except ValidationError as e:
        print(e.json())
        pytest.fail()
