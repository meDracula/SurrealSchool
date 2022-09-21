from person import Person
from schedular import Schedular


class Teacher(Person, Schedular):
    def __init__(self, admin):
        self.admin = admin

    def set_student_grade(self, student_name, course, grade):
        self.admin.grading(student_name, course, grade)
