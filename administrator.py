import json


class Administrator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = Administrator.__init__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, courses, classrooms, computer_asset):
        self.courses = courses
        self.grading_db = 'db.json'
        self.classrooms = classrooms
        self.computer_asset = computer_asset
        return self

    def grading(self, student_name, course, grade):
        if course not in self.courses:
            raise ValueError("Not a vaild course")

        student = json.loads({ student_name: { course: grade } })
        # create, update
        with open(self.grading_db, 'r', encoding='utf-8') as file:
            data = json.loads(f.readline())
            stud = data.get(student.keys(), None)
            if stud is None:
                # create student
                pass
            else:
                # update
                with open(self.grading_db, 'a', encoding='utf-8') as file:
                    json.dump(student, file)

    def delete_grading(self):
        # delete
        pass

    def get_student_grading(self, name):
        with open(self.grading_db, 'r', encoding='utf-8') as file:
            data = json.loads(f.readline())
            return data[name]


if __name__ == '__main__':
    admin = Administrator(['math', 'physics', 'bio'], ["a1"], "laptop")
    print(admin)
