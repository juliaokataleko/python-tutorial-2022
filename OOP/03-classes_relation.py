
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

# define instances
s1 = Student("Julian", 27, 18)
s2 = Student("Isabel", 25, 19)
s3 = Student("Floripa", 1, 20)

c1 = Course("Math", 2)
c1.add_student(s1)
c1.add_student(s2)
average = c1.get_average_grade()

print("Course ", c1.name, " average: ", average)
