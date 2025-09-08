# Data Abstraction
"""
Abstraction hides the internal implementation details while exposing only the
necessary functionality. It helps focus on "what to do" rather than "how to do it."

>>> Types of Abstraction:
$ Partial Abstraction: Abstract class contains both abstract and concrete methods.
$ Full Abstraction: Abstract class contains only abstract methods (like interfaces).

Example: In this example, we create an abstract Dog class with an abstract
method(sound) and a concrete method. Subclasses implement the abstract method while inheriting the concrete method.
"""
from abc import ABC, abstractmethod
class Dog(ABC): # Abstract Class
	def __init__(self, name):
		self.name = name 

	@abstractmethod
	def sound(self): # Abstract Method
		pass	

	def display_name(self): # Concrete Method
		return f"Dog's name: {self.name}"

class Lbrador(Dog): # Partial Abstraction
	def sound(self):
		return "Lbrador Woof!"

class Beagle(Dog):  # Partial Abstraction
	def sound(self): 
		return "Beagle Bark!"


# Just for test purpose
class Desi(Dog):
	name = "Desi Dog"
	#def sound(self):
	#	return "Desi Woof!"


# Example Usage

dogs = [Lbrador("Jonny"), Beagle("Charile"), Desi("Desi")]
for dog in dogs:
	print(dog.display_name()) # Calls concrete method
	print(dog.sound()) # Calls implemented abstract method
		



		