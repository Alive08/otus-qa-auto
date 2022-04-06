from csv import reader, DictReader
from genericpath import exists
from itertools import count
import json


books_file = "src/books/data/books.csv"
users_file = "src/books/data/users.json"
result_file = "src/books/data/result.json"

USER_FIELDS = ('name', 'gender', 'age', 'address', 'books', 'books_count')


def gen_csv(file):
    with open(file, newline='', mode='r') as f:
        for line in DictReader(f):
            yield line

# более короткая, но менее безопасная форма генератора книг
# books = (row for row in DictReader(open(books_file, newline='', mode='r')))


def gen_json(file):
    with open(file, mode='r') as f:
        for entry in json.load(f):
            entry['books'] = []
            entry['books_count'] = 0
            yield dict(filter(lambda i: i[0] in USER_FIELDS, entry.items()))


if __name__ == '__main__':

    i = 0
    total_books = 0
    users = list(gen_json(users_file))
    for b in gen_csv(books_file):
        try:
            users[i]
        except IndexError:
            i = 0
        users[i]['books'].append(b)
        users[i]['books_count'] += 1
        i += 1
        total_books += 1
    del i

    with open(result_file, mode='r') as f:
        try:
            json.dump(users, f, indent=4)
        except Exception as e:
            print(e)
        else:
            print(
                f"Готово: распределено {total_books} книг между {len(users)} пользователями")
