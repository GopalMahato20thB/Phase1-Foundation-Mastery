# Python Inheritance
"""
Inheritance allows a class (child class) to acquire properties and methods of 
another class (parent class). It supports hierarchical classification and promotes
code reuse.

>>> Types of Inheritance: 
1. Single Inheritance: A child class inherits from a single parent class.
2. Multiple Inheritance: A child class inherits from more than one parent class.
3. Multilevel Inheritance: A child class inherits from a parent class, which in turn
inherits from another class.
4. Hierarchical Inheritance: Multiple child class inherits from a single parent class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.

>>> Example: In this example, we create a Dog class and demonstrate single, multilevel and multiple inheritance.
We show how child classes can use or extend parent class methods.

"""
# Single Inheritance
class Dog:
	def __init__(self, name):
		self.name = name 

	def display_name(self):
		return f"Dog's name: {self.name}"	

class labrador(Dog):
	def sound(self):
		return f"{self.name} says woof!"

o1 = labrador("Jhony")
print(o1.sound())		

print("-----"*12)

# Multiple Inheritance
class Friendly:
	def greet(self):
		return "Friendly"


class GoldenRetriver(Dog, Friendly): #Multiple Inheritance
	def sound(self):
		return "Golden  Retriver Barks"


retriver =GoldenRetriver("Charlie")
print(retriver.display_name())
print(retriver.greet())
print(retriver.sound())


