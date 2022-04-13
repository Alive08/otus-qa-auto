import pytest
from requests import request
from src.api.simple_api_client import SimpleApiClient
from jsonschema import validate
from jsonschema.exceptions import ValidationError

base_url = 'https://api.openbrewerydb.org/breweries'


proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080"
}


single_brewery_schema = {
    "type": "object",
    "required": ["id", "name", "brewery_type",
                 "city", "state",  "country",
                 "updated_at", "created_at"],
    "properties": {
        "id": {"type": ["integer", "string"]},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": ["string", "null"]},
        "address_2": {"type": ["string", "null"]},
        "address_3": {"type": ["string", "null"]},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {"type": ["string", "null"]},
        "postal_code": {"type": ["string", "number"]},
        "country": {"type": "string"},
        "longitude": {"type": ["string", "null"]},
        "latitude": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "website_url": {"type": ["string", "null"]},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }
}


multiple_brewery_schema = {
    "type": "array",
    "items": single_brewery_schema
}


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
        validate(instance=brewery_list, schema=single_brewery_schema)
    except ValidationError as err:
        raise AssertionError from err
    print(brewery_list)


def test_brewery_search(api):
    api.GET('/search', params={'query': 'dog'})
    assert api.check_if_success()
    assert api.validate_json(schema=multiple_brewery_schema)

