import pytest
from src.api.simple_api_client import SimpleApiClient

base_url = 'https://dog.ceo/api'

proxies = {
    "http": "http://vkozlov:8080",
    "https": "http://vkozlov:8080"
}

dogs_api_schema = {

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
    }
}

# full list of breeds with sub-breeds
raw_breeds_list = SimpleApiClient(url=base_url, verify=False, proxies=None).GET(
    '/breeds/list/all').json()['message']


def breeds(res):
    for breed, val in res.items():
        for subbreed in val:
            yield breed, subbreed


def idfn(val):
    if isinstance(val, str):
        return val.title()
    if isinstance(val, tuple):
        return f'{val[1].title()} {val[0].title()}'
    return val


@pytest.fixture(params=set(b for b, dummy in breeds(raw_breeds_list)), ids=idfn, scope='session')
def breed(request):
    yield request.param


@pytest.fixture(params=breeds(raw_breeds_list), ids=idfn, scope='session')
def sub_breed(request):
    yield request.param


@pytest.fixture(scope='session')
def api():
    def success_validator(obj):
        return obj.response.json()['status'] == 'success'

    yield SimpleApiClient(url=base_url, verify=False, proxies=proxies, validator=success_validator)

# --- tests without sub-breads


def test_breeds_list(api):
    api.GET('/breeds/list')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_array_string'])


def test_breeds_list_all(api):
    api.GET('/breeds/list/all')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_dict_array_string'])


def test_breeds_image_random(api):
    api.GET('/breeds/image/random')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_string'])


@pytest.mark.parametrize('n', range(1, 3))
def test_breeds_image_random_multiple(api, n):
    api.GET(f'/breeds/image/random/{n}')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_array_string'])

# --- tests with sub-breads


def test_breed_list(api, breed):
    api.GET(f'/breed/{breed}/list')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_array_string'])


def test_breed_images_all(api, breed):
    api.GET(f'/breed/{breed}/images')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_array_string'])


def test_breed_image_random(api, breed):
    api.GET(f'/breed/{breed}/images/random')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_string'])


@pytest.mark.parametrize('n', range(1, 3))
def test_breed_image_random_multiple(api, breed, n):
    api.GET(f'/breed/{breed}/images/random/{n}')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_array_string'])


# --- tests on images with sub-breads


def test_breed_sub_breed_images(api, sub_breed):
    api.GET(f'/breed/{sub_breed[0]}/{sub_breed[1]}/images')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_array_string'])


def test_breed_sub_breed_images_random(api, sub_breed):
    api.GET(f'/breed/{sub_breed[0]}/{sub_breed[1]}/images/random')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_string'])


@pytest.mark.parametrize('n', range(1, 3))
def test_breed_sub_breed_images_random_multiple(api, n, sub_breed):
    api.GET(f'/breed/{sub_breed[0]}/{sub_breed[1]}/images/random/{n}')
    assert api.check_if_success()
    assert api.validate_json(schema=dogs_api_schema['dict_array_string'])
