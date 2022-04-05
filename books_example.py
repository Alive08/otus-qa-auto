from src.books.classes import Book, Person, Reader


b = Book()
print(b.__dict__)

b.author = "John Smith"
b.genre = "fantasy"
b.pages = 101
b.title = "Too hard to die"

print(b.__dict__)