import json
import pytest

reference_file = 'src/books/data/reference.json'
result_file = 'src/books/result.json'


@pytest.fixture
def reference_entry():
    with open(reference_file, mode='r') as f:

        yield json.load(f).pop()


@pytest.fixture
def readers_data():
    with open(result_file, mode='r') as f:

        yield json.load(f)


def test_user_entry_struture(reference_entry, readers_data):
    '''
    тест проверяет каждую запись о пользователе
    в файле results.json на соответствие структуре
    референсной записи reference.json, включая
    проверку типов соответствующих аттрибутов
    '''
    for user in readers_data:
        assert isinstance(user, dict)

        assert user.keys() == reference_entry.keys()

        for k, v in user.items():
            assert type(v) == type(reference_entry[k])

        for book in user['books']:
            assert isinstance(book, dict)
            assert book.keys() == reference_entry['books'][0].keys()
            reference_book = reference_entry['books'][0]
            for k, v in book.items():
                assert type(v) == type(reference_book[k])
