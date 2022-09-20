from person import Person
from schedular import Schedular
from administrator import Administrator


class Teacher(Person, Schedular):
    def set_student_grade(self, student_name, course, grade):

        Administrator().grading(student)


if __name__ == '__main__':
    admin = Administrator(['math', 'physics', 'bio'], ["a1"], "laptop")
    teacher = Teacher()
    teacher.set_student_grade("steve", "math", "A")
