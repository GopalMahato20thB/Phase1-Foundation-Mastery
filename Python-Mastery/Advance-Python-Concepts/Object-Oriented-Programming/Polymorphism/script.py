# Polymorphism
"""
Polymorphism allows methods to have the same but behave deffierently based
on the object's context. It can be achieved through method overriding or overloading.

>>> Types of Polymorphism
1. Compile-Time Polymorphism: This type of polymorphism is determined during
the compilation of the program. It allows methods or operators with the same name
to behave differrntly based on their input parameter or usage. It is commonly referred 
to as method or operator overloading.
2. Run-Time Polymorphism: This type of polymorphism is determined during the
execution of the program. It occurs when a subclass provides a specific 
implementation for a method already defined in its parent class, commonly 
known as method overriding.

Example: In this example, we show run-time polymorphism using method
overriding with dog classes and compile-time polymorphism by mimicking
method overloading in a calculator class.
"""
# Parent class 
class Dog:
	def sound(self): # default implementation
		return "Dog Sound!"


# Run-Time polymorphism: Method Overriding
class Labrador(Dog):
	def sound(self): # Overriding parent method
		return "Labrador Woofs!"


class Beagle(Dog):
	def sound(self): # Overriding parent method
		return "Beagle Barks!" 				


# Compile-Time Polymorphism: Method Overloading Mimic

class Calculator:
	def add(self, a, b=0, c=0): 
		return a + b + c # supports multiple ways to call add()


# Run-Time Polymorphism
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
	print(dog.sound()) # Calls the appropriate method based on the object type

# Compile-Time Polymorphism (Mimicked using default arguments)

calc = Calculator()
print(calc.add(5, 7)) # two arguments
print(calc.add(7, 7, 7)) # three argument


