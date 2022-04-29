import json

import pytest
from pydantic import BaseModel, StrictInt, ValidationError

result_file = 'src/books/result.json'


class Book(BaseModel):
    title: str
    author: str
    genre: str
    pages: StrictInt


class Person(BaseModel):
    name: str
    gender: str
    address: str
    age: StrictInt


class BookReader(Person):
    books: list[Book]


def gen_users(file):
    with open(file, mode='r') as f:
        for user in json.load(f):
            yield user


@pytest.fixture(params=gen_users(result_file), ids=lambda val: val['name'], scope='session')
def user(request):
    yield request.param


def test_every_user_entry_schema(user):
    '''
    тест проверяет каждую запись о пользователе
    в файле results.json на соответствие схеме
    '''
    try:
        BookReader.parse_obj(user)
    except ValidationError as e:
        print(e.json())
        pytest.fail()
