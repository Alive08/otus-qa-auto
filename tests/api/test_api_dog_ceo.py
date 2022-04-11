from hamcrest import *
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import pytest
from src.api.simple_api_client import SimpleApiClient, proxies

base_url = 'https://dog.ceo/api'


api_schema = {

    'dict_string': {
        "type": "object",
        "required": ["message", "status"],
        "properties": {
            "status": {"type": "string"},
            "message": {"type": "string"}
        }
    },

    'dict_array_string': {
        "type": "object",
        "required": ["message", "status"],
        "properties": {
            "status": {"type": "string"},
            "message": {
                "type": "array",
                "minItems": 1,
                "items": {"type": "string"}
            }
        }
    },

    'dict_dict_array_string': {
        "type": "object",
        "required": ["message", "status"],
        "properties": {
            "status": {"type": "string"},
            "message": {
                "type": "object",
                "minProperties": 1,
                "patternProperties": {
                    "^[a-z]+$": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                }
            }
        }
    },


}


@pytest.fixture
def api():

    yield SimpleApiClient(url=base_url, verify=False, proxies=proxies)


def test_breeds_list(api):
    r = api.GET('/breeds/list')
    assert r.status_code == 200
    assert r.json()['status'] == 'success'
    try:
        validate(instance=r.json(), schema=api_schema['dict_array_string'])
    except ValidationError as err:
        raise AssertionError
    print(r.json())

def test_breeds_list_all(api):
    r = api.GET('/breeds/list/all')
    assert r.status_code == 200
    assert r.json()['status'] == 'success'
    try:
        validate(instance=r.json(),
                 schema=api_schema['dict_dict_array_string'])
    except ValidationError as err:
        raise AssertionError



def test_breeds_image_random(api):
    r = api.GET('/breeds/image/random')
    j = r.json()
    assert r.status_code == 200
    assert j['status'] == 'success'
    try:
        validate(instance=r.json(), schema=api_schema['dict_string'])
    except ValidationError as err:
        raise AssertionError from err


@pytest.mark.parametrize('n', range(1, 4))
def test_breeds_image_random_multiple(n, api):
    with api.GET(f'/breeds/image/random/{n}') as r:
        j = r.json()
        assert r.status_code == 200
        assert j['status'] == 'success'
        assert len(j['message']) == n
    try:
        validate(instance=r.json(), schema=api_schema['dict_array_string'])
    except ValidationError as err:
        raise AssertionError


def test_breed_hound_images_all(api):
    r = api.GET('/breed/hound/images')
    j = r.json()
    assert r.status_code == 200
    assert j['status'] == 'success'
    try:
        validate(instance=r.json(), schema=api_schema['dict_array_string'])
    except ValidationError as err:
        raise AssertionError


def test_breed_hound_image_random(api):
    r = api.GET('/breed/hound/images/random')
    j = r.json()
    assert r.status_code == 200
    assert j['status'] == 'success'
    try:
        validate(instance=r.json(), schema=api_schema['dict_string'])
    except ValidationError as err:
        raise AssertionError


@pytest.mark.parametrize('n', range(1, 4))
def test_breed_hound_image_random_multiple(n, api):
    with api.GET(f'/breed/hound/images/random/{n}') as r:
        j = r.json()
        assert r.status_code == 200
        assert j['status'] == 'success'
        assert type(j['message']) == list
        assert len(j['message']) == n
    try:
        validate(instance=r.json(), schema=api_schema['dict_array_string'])
    except ValidationError as err:
        raise AssertionError


def test_breed_hound_list(api):
    r = api.GET('/breed/hound/list')
    j = r.json()
    assert r.status_code == 200
    assert j['status'] == 'success'
    try:
        validate(instance=r.json(), schema=api_schema['dict_array_string'])
    except ValidationError as err:
        raise AssertionError


breed_list = SimpleApiClient(url=base_url, verify=False, proxies=proxies).GET(
    '/breed/hound/list').json()['message']


@pytest.fixture(params=breed_list)
def get_breed(request):

    yield request.param


# в этот тест передается параметризованная фикстура (get_bread)
def test_breed_hound_sub_bread_images(api, get_breed):
    r = api.GET(f'/breed/hound/{get_breed}/images')
    j = r.json()
    assert r.status_code == 200
    assert j['status'] == 'success'
    try:
        validate(instance=r.json(), schema=api_schema['dict_array_string'])
    except ValidationError as err:
        raise AssertionError


def test_breed_hound_sub_bread_images_random(api, get_breed):
    r = api.GET(f'/breed/hound/{get_breed}/images/random')
    j = r.json()
    assert r.status_code == 200
    assert j['status'] == 'success'
    try:
        validate(instance=r.json(), schema=api_schema['dict_string'])
    except ValidationError as err:
        raise AssertionError


@pytest.mark.parametrize('n', range(1, 4))
def test_breed_hound_sub_bread_images_random_n(n, api, get_breed):
    r = api.GET(f'/breed/hound/{get_breed}/images/random/{n}')
    j = r.json()
    assert r.status_code == 200
    assert j['status'] == 'success'
    try:
        validate(instance=r.json(), schema=api_schema['dict_array_string'])
    except ValidationError as err:
        raise AssertionError

