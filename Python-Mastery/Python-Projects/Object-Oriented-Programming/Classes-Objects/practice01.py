#1. Create a `Book` class with attributes `title`, `author`, and `price`. Add a method `display_info()` to print details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"Book Title: {self.title} | Author: {self.author} | Price: {self.price}"


my_books01 = Book("Think and Grow Rich", "Napolean Hill", 175)
print(my_books01.display_info())




