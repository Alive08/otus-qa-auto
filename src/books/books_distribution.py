from csv import DictReader
from functools import reduce
import json


books_file = "src/books/data/books.csv"
users_file = "src/books/data/users.json"
result_file = "src/books/result.json"

USER_ATTRS= ('name', 'gender', 'age', 'address', 'books')


def gen_csv(file):
    with open(file, newline='', mode='r') as f:
        for line in DictReader(f):
            yield line


def gen_json(file):
    with open(file, mode='r') as f:
        for entry in json.load(f):
            entry['books'] = []
            yield dict(filter(lambda i: i[0] in USER_ATTRS, entry.items()))


if __name__ == '__main__':

    i = 0
    total_books = 0
    users = list(gen_json(users_file))
    for b in gen_csv(books_file):
        try:
            t = users[i]
        except IndexError:
            i = 0
        users[i]['books'].append(b)
        total_books += 1
        i += 1
    del i

    with open(result_file, mode='w') as f:
        try:
            json.dump(users, f, indent=4)
        except Exception as e:
            print(e)
        else:
            print(
                f"Распределено {total_books} книг между {len(users)} читателями")
