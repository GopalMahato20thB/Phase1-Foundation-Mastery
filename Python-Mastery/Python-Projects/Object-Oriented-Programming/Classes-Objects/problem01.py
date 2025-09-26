"""
## Practice Problems
- 1. Create a class Person with attributes name and age . Initialize them in the constructor and
add a method greet that prints a greeting message including the name and age.
"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age 

	def greet(self):
		return f"Hello {self.name} You are {self.age} years old!"


p1 = Person("Gopal Mahato", 19)
print(p1.greet())

p2 = Person("Ujjwal Das", 19)
print(p2.greet())

p3 = Person("Yubraj Sing Sardar", 21)
print(p3.greet())
