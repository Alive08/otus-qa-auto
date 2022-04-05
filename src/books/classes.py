from typing import List
from src.descriptors import GenderData, AgeData, NameData, NonNegative, StringData


class Person:

    name = NameData()
    gender = GenderData()
    age = AgeData()
    address = StringData()

    def __init__(self, name='unknown', gender='unknown', age=None, address='unknown'):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address

    @classmethod
    def restore_from_json(cls, json_data):
        pass

    def save_to_json(self, json_data):
        pass


class Book:

    __count = 0

    title = StringData()
    author = NameData()
    pages = NonNegative()
    genre = StringData()
    current_reader = NameData()

    def __init__(self, title='unknown', author='unknown', pages=2, genre='unknown'):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.leased = False
        self.current_reader = None
        type(self).__count += 1

    def __del__(self):
        type(self).__count -= 1
    
    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def restore_from_csv(cls, string):
        pass

    def save_to_csv(self, json_data):
        pass



class Reader(Person):

    __count = 0

    def __init__(self, name='unknown', gender='unknown', age=None, address='unknown'):
        super().__init__(name, gender, age, address)
        self.books = []
        type(self).__count += 1

    def __del__(self):
        type(self).__count -= 1

    @classmethod
    def get_count(cls):
        return cls.__count

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, lst):
        if not isinstance(lst, List):
            raise ValueError
        self.__books = lst

    def borrow_a_book(self, book):
        if not isinstance(book, Book):
            raise ValueError
        self.books.append(book)
        book.current_reader = self.name
        book.leased = True

    def return_a_book(self, idx):
        try:
            book = self.books.pop(idx)
        except:
            return
        else:
            book.leased = False
            book.current_reader = None

    def return_all_books(self):
        for b in enumerate(self.books):
            self.return_a_book(b)

    @classmethod
    def restore_from_json(cls, json_data):
        
        pass

    def save_to_json(self):
        pass
