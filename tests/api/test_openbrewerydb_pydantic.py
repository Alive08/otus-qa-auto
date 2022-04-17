from email.policy import strict
from enum import Enum
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from pydantic import (BaseModel, HttpUrl, StrictInt, StrictStr,
                      ValidationError, conlist)
from requests import request
from src.api.simple_api_client import SimpleApiClient

base_url = 'https://api.openbrewerydb.org/breweries'


proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080"
}


class BreweryType(Enum):
    micro = 'micro'
    nano = 'nano'
    regional = 'regional'
    brewpub = 'brewpub'
    large = 'large'
    planning = 'planning'
    bar = 'bar'
    contract = 'contract'
    proprieter = 'proprieter'
    closed = 'closed'


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: BreweryType
    street: str = None
    address_2: str = None
    address_3: str = None
    city: str
    state: str = None
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
    __root__: list[Brewery]


def validate_object(cls, obj):
    try:
        cls.parse_obj(obj)
    except ValidationError as e:
        print(e.json())
        pytest.fail()


@pytest.fixture(scope='session')
def api():
    yield SimpleApiClient(url=base_url, verify=False, proxies=proxies)


def breweries():
    with SimpleApiClient(url=base_url, verify=False, proxies=None).GET('/') as r:
        for j in r.json():
            yield j


@pytest.fixture(params=breweries(), ids=lambda v: v['name'], scope='session')
def brewery(request):
    yield request.param


def test_brewery_list_all(brewery):
    validate_object(Brewery, brewery)


def test_brewery_search(api):
    r = api.GET('/search', params={'query': 'dog'})
    assert r.ok
    for item in r.json():
        validate_object(Brewery, item)


@pytest.mark.parametrize('brewery_type', [bt.value for bt in BreweryType])
def test_brewery_search_by_type(api, brewery_type):
    r = api.GET('/', params={'by_type': brewery_type})
    assert r.ok
    validate_object(BreweryList, r.json())


@pytest.mark.parametrize('city', ['Evergreen'])
def test_brewery_search_by_city(api, city):
    r = api.GET('/', params={'by_city': city})
    assert r.ok
    validate_object(BreweryList, r.json())


# by_city
# by_dist
# by_name
# by_state
# by_postal
# by_type

# page
# per_page
# sort
# get a single brewery
# breweries/search?query=dog - search
# /breweries/autocomplete?query=dog - autocomplete
