from person import Person
from schedular import Schedular
import sys


class Student(Person, Schedular):
    __slots__ = 'courses', 'grades'

    def __init__(self):
        self.courses = set()
        self.grades = {}

    def add_courses(self, *args):
        self.courses.update(args)

    def remove_courses(self, *args):
        self.courses -= self.courses.intersection(set(args))
