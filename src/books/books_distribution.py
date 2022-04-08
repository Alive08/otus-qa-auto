import json
from csv import DictReader

books_file = "src/books/data/books.csv"
users_file = "src/books/data/users.json"
result_file = "src/books/result.json"
reference_file = "src/books/data/reference.json"

USER_ATTRS = ('name', 'gender', 'address', 'age', 'books')
BOOK_ATTRS = ('title', 'author', 'pages', 'genre')

try:
    with open(reference_file, mode='r') as f:
        entry = json.load(f).pop()
except(FileNotFoundError, IndexError):
    print('Error: the reference file is unavailable, will use default attrs')
else:
    print('Will use user\'s and book\'s attrs from the reference file')
    USER_ATTRS = tuple(entry.keys())
    BOOK_ATTRS = tuple(entry['books'].pop().keys())


def tryconvert(*types):
    def convert(value):
        for t in types:
            try:
                return t(value)
            except (ValueError, TypeError):
                continue
        return value
    return convert


def gen_csv(file):
    with open(file, newline='', mode='r') as f:
        for d in DictReader(f):
            yield {k.lower(): tryconvert(int)(v)
                   for k, v in d.items() if k.lower() in BOOK_ATTRS}


def gen_json(file):
    with open(file, mode='r') as f:
        for entry in json.load(f):
            entry['books'] = []
            yield {k: v for k, v in entry.items() if k in USER_ATTRS}


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
                f"{total_books} books have been distributed among {len(users)} users")
