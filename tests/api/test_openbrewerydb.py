import pytest
from requests import request
from src.api.simple_api_client import SimpleApiClient
from jsonschema import validate
from jsonschema.exceptions import ValidationError

base_url = 'https://api.openbrewerydb.org'

proxies = {
    "http": "http://vkozlov:8080",
    "https": "http://vkozlov:8080"
}


brewery_schema = {
    "type": "object",
    "required": ["id", "name", "city", "country"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {"type": "string"},
        "address_3": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {"type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "float"},
        "latitude": {"type": "float"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }
}


@pytest.fixture(scope='session')
def api():

    yield SimpleApiClient(url=base_url, verify=False, proxies=proxies)


def breweries():
    with SimpleApiClient(url=base_url, verify=False, proxies=None).GET('/breweries') as r:
        for j in r.json():

            yield j


@pytest.fixture(params=breweries(), ids=lambda v: v['name'], scope='session')
def brewery_list(request):
    yield request.param


def test_brewery_list_all(brewery_list):
    try:
        validate(instance=brewery_list, schema=brewery_schema)
    except ValidationError as err:
        raise AssertionError from err
