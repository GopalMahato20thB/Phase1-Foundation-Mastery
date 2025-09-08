"""
- 5. Design a class Car with attributes make , model , and year . Add a method display_info
that prints all attributes. Create an object and demonstrate. 
"""
class Car:

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def display_info(self):
		return f"Brand: {self.make} | Model: {self.model} | Year: {self.year}"

c1 = Car("Lamborgini", "Urus", "2025")
print(c1.display_info())

