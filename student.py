from person import Person
from schedular import Schedular
import sys
#from administrator import Administrator


class Student(Person, Schedular):
    __slots__ = 'courses', 'grades'

    def __init__(self):
        self.courses = set()
        self.grades = {}

    def add_courses(self, *args):
        self.courses.update(args)

    def remove_courses(self, *args):
        self.courses -= self.courses.intersection(set(args))

    def get_admin(self):
        #return Administrator()
        pass

if __name__ == '__main__':
    student = Student()
    student.add_courses('math', 'physics', 'bio')
    print(student.courses)
    student.remove_courses('bio')
    print(student.courses)
    print(student.__dict__)
