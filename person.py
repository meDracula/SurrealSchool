from collections import namedtuple


class Person:
    def __init__(self, first_name, last_name, birthday):
        self.id = self.generate_id()
        self.name = namedtuple('name', ['first_name', 'last_name'])
        self.birthday = birthday

    @classmethod
    def generate_id(cls):
        return 5
