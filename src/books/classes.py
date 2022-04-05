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
    def get_from_json(cls, json_data):
        pass


class Book:

    __count = 0

    title = StringData()
    author = NameData()
    pages = NonNegative()
    genre = StringData()

    def __init__(self, title='unknown', author='unknown', pages=2, genre='unknown'):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    @classmethod
    def get_from_csv(cls, string):
        pass


class Reader(Person):

    __count = 0

    def __init__(self, name='unknown', gender='unknown', age=None, address='unknown'):
        super().__init__(name, gender, age, address)
        self.books = []

    @property
    def books(self):
        pass

    @classmethod
    def get_from_json(cls, json_data):
        pass

    def put_to_json(self):
        pass
