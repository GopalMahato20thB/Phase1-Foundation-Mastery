# You have a list of student marks. Write a function to return grades based on conditions: >=90 → "A", >=75 → "B", >=50 → "C", else "Fail".

def grades(marks):
    average_marks = sum(marks) / len(marks)

    if average_marks >= 90 and average_marks <= 100:
        grade = "A"
    elif average_marks >= 75 and average_marks < 90:
        grade = "B"
    elif average_marks >= 50 and average_marks < 75:
        grade = "C"
    else:
        grade = "Fail"
    return grade
print(grades([97, 98, 99, 95, 100, 100, 100]))
