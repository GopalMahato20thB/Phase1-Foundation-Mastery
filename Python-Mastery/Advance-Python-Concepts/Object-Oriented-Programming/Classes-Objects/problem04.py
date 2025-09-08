"""
- 4. Create a class Student with attributes name and grades (a list). Add a method
average_grade that computes the average of the grades. Instantiate an object and call the
method.
"""

class Student:

	def __init__(self, name, grade):
		self.name = name
		self.grade = grade 

	def average_grade(self):
		average = sum(self.grade) / len(self.grade)
		return average

gopal = Student("Gopal Mahato", [95, 85, 75])
print(gopal.average_grade())
		 


			
