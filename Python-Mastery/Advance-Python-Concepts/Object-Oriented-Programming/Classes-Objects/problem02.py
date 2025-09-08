"""
- 2. Define a class Book with attributes title , author , and year . Create two objects from this
class and print their details.

"""

class Book:
	def __init__(self, title, author, year):
		self.title = title
		self.author = author 
		self.year = year

	def details(self):
		return f"Book title: {self.title} | Author: {self.auhtor} | Year: {self.year}"


