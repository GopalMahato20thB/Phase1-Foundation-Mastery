# 3. Create a `Circle` class with a method to compute area and circumference. Instantiate multiple circles with different radii.


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area_circumference(self):
        return f"Area: {3.14*(self.radius*self.radius)} | Circumference: {2*3.14*self.radius}"


c1 = Circle(7)
print(c1.area_circumference())
c1 = Circle(7)
print(c1.area_circumference())
c1 = Circle(9)
print(c1.area_circumference())
c1 = Circle(4)
print(c1.area_circumference())
