from src.books.classes import Book, Person, Reader
from copy import copy
import json
from src.books.classes import Person

person_data = 'src/books/person_record.json'


j = None

with open(person_data, 'r') as f:
    j = json.load(f)

r = Reader.import_from_json(j)

print(r.__dict__)




