"""
- 3. Build a class Rectangle with attributes length and width . Add a method area to
calculate and return the area of the rectangle. Test it with an object.
"""
class Rectangle:

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width


ob1 = Rectangle(7, 4)
print(ob1.area())
			

