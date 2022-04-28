import json
from csv import DictReader
from time import time
from functools import reduce

books_file = "src/books/books.csv"
users_file = "src/books/users.json"
result_file = "src/books/result.json"

USER_ATTRS = ('name', 'gender', 'address', 'age', 'books')
BOOK_ATTRS = ('title', 'author', 'pages', 'genre')


def benchmark(func):

    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        t = end - start
        print('Время выполнения:', t)
        return result

    return wrapper


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


@benchmark
def run():
    gen_users = gen_json(users_file)
    gen_books = gen_csv(books_file)
    users = []

    '''i = 0
    users = list(gen_json(users_file))
    for b in gen_csv(books_file):
        try:
            t = users[i]
        except IndexError:
            i = 0
        users[i]['books'].append(b)
        i += 1'''

    # for test
    # list(gen_users)
    # list(gen_books)

    for book in gen_books:          # извлекаем книги из генератора до исчерпания
        try:
            user = next(gen_users)  # извлекаем юзера из генератора
        except StopIteration:       # если генератор юзеров исчерпан,
            try:
                user = users.pop(0) # берем первый элемент списка юзеров
            except IndexError:      # список юзеров пуст, возможно пустой файл
                break               # некому раздавать, заканчиваем
        users.append(user)          # добавляем юзера в конец списка
        user['books'].append(book)  # добавляем юзеру книгу

    with open(result_file, mode='w') as f:
        try:
            json.dump(users, f, indent=4)
        except Exception as e:
            print(e)
        else:
            print(
                f"{reduce(lambda x, y: x + len(y['books']), users, 0)} books have been distributed among {len(users)} users")
                # sum(map(len, (u['books'] for u in users)))

if __name__ == '__main__':

    run()
