"""
name = "Gopal Mahato"
age = 19

print(type(name), type(age))
 # name is from string class  
 # age is from string class 
 # name and age are just instance or object of string and int class 


 # creating dog class

class Dog:
    def bark(self):
        print("Whoof Whoof")

jhonny = Dog()
print(type(jhonny)) 

jhonny.bark()      


## using a constructor

class Dog2:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


    def bark(self):
        return f"{self.name} is barking!"


### creating owner object

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

owner1 = Owner("Gopal Mahato", "Purulia, WestBangal", 6296822675)
sit = Dog2("Mr. Sit", "general", owner1) # i think breed means the type thats why i typed this instance of dog is a general dog.
print(sit.bark())

dog_2 = Dog2("Mr. Pop", "general",owner1)


print(dog_2.owner.name)
print(dog_2.owner.address, dog_2.owner.contact_number)

"""

# Another Example:
class Dog:
    species = "Canine" # Class Attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.age)
print(dog1.species)
        




                 
