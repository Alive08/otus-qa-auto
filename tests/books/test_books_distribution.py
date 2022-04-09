import json
import jsonschema
import pytest


reference_file = 'src/books/data/reference.json'
result_file = 'src/books/result.json'


@pytest.fixture(scope='module')
def user_schema():
    return {
        "type": "object",
        "properties": {
                "name": {"type": "string"},
                "gender": {"type": "string"},
                "address": {"type": "string"},
                "age": {"type": "integer"},
                "books": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": True,
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "author": {"type": "string"},
                            "pages": {"type": "integer"},
                            "genre": {"type": "string"}
                        },
                        "required": ["title", "author", "pages", "genre"]
                    }
                }
        },
        "required": ["name", "gender", "address", "age", "books"]
    }


@pytest.fixture
def reference_entry():
    with open(reference_file, mode='r') as f:

        yield json.load(f).pop()


def users():
    with open(result_file, mode='r') as f:
        for user in json.load(f):

            yield user


def test_reference_for_schema(reference_entry, user_schema):
    '''
    Тест проверяет валидность референсного файла
    '''
    try:
        jsonschema.validate(instance=reference_entry, schema=user_schema)
    except jsonschema.exceptions.ValidationError as err:
        raise AssertionError


@pytest.mark.parametrize("user", [u for u in users()])
def test_every_user_entry_struture(user, user_schema):
    '''
    тест проверяет каждую запись о пользователе
    в файле results.json на соответствие схеме
    '''
    try:
        jsonschema.validate(instance=user, schema=user_schema)
    except jsonschema.exceptions.ValidationError as err:
        raise AssertionError
