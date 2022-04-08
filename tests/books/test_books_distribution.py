import json

import pytest

USER_ATTRS = ('name', 'gender', 'address', 'age', 'books')
BOOK_ATTRS = ('title', 'author', 'pages', 'genre')


@pytest.fixture
def reference_entry():
    reference_file = 'src/books/data/reference.json'
    with open(reference_file, mode='r') as f:

        yield json.load(f).pop()


@pytest.fixture
def readers_data():
    json_file = 'src/books/result.json'
    with open(json_file, mode='r') as f:

        yield json.load(f)


def test_user_entry_struture(reference_entry, readers_data):
    '''
    тест проверяет каждую запись о пользователе
    в файле results.json на соответствие структуре
    референсной записи reference.json
    '''
    for user in readers_data:
        assert isinstance(user, dict)
        assert user.keys() == reference_entry.keys()

        for k, v in user.items():
            assert type(v) == type(reference_entry[k])

        for book in user['books']:
            assert isinstance(book, dict)
            reference_book = reference_entry['books'][0]

            for k, v in book.items():
                print(v, type(v), '---', reference_book[k], type(reference_book[k]))
            #     assert type(v) == type(reference_book[k])

            assert book.keys() == reference_entry['books'][0].keys()
