"""A program for calculating grades. Debug testing."""


def process_students(student_data):
    """Takes a list of dictionary entries for {students/grades} 
        and returns a tuple of (name, grade)."""
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    """Takes a list of grades and returns the average."""
    total = sum(grades)
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

def collect_grades(students):
    """pulls grades out of a list of students using proces_students, then 
        returns a list of grades."""
    grades = []
    for student in students:
        name, grade = process_students(student)
        if grade:
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))
