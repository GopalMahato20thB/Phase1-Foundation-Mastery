# 4. Write a `Student` class with attributes `name`, `roll_no`, and `marks`. Add a method `get_grade()` that returns grade based on marks.

class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def get_grade(self):
        average_marks = sum(self.marks) / len(self.marks)
        if average_marks >= 90 and average_marks <= 100:
            grade = "A"
        if average_marks < 90 and average_marks >= 80:
            grade = "B"
        if average_marks < 80 and average_marks >= 70:
            grade = "C"
        if average_marks < 70 and average_marks >= 60:
            grade = "D+"
        if average_marks < 60 and average_marks >= 50:
            grade = "D-"
        if average_marks < 50:
            grade = "F"

        return grade, f"Average Marks: {average_marks}"




    def student_info(self):
        return f"Name: {self.name}\nRoll No. {self.roll_no}\nMarks: {self.marks}\nGrade: {self.get_grade()}"


s1 = Student("Gopal Mahato", 1, [95, 85, 84, 75, 74])
print(s1.student_info())
s2 = Student("Gopal Mahato", 1, [65, 75, 69, 66, 87])
print(s2.student_info())

