#5. Create a `Car` class with attributes like `make`, `model`, `year`, and a method `start_engine()`.

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.make} {self.model}({self.year}) engin started!"


laborgini = Car("Lamborgini", "Revuelto", 2024)
print(laborgini.start_engine())
