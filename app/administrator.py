from teacher import Teacher


class Administrator:
    _instance = None
    grades = ("F", "E", "D", "C", "B", "A")

    def __init__(self, courses, classrooms, computer_asset):
        self.courses = courses
        self.classrooms = classrooms
        self.computer_asset = computer_asset

    def grading(self, student_name: str, course: str, grade: str) -> None:
        assert course in self.courses, ValueError("Not a vaild course")
        assert grade in self.grades, ValueError("Not a vaild grade")

        student = { student_name: { course: grade } }
        print(student)
        # TODO create student if not exists else update with new course and grade

    def delete_grading(self):
        # delete
        pass

    def get_student_grading(self, name):
        with open(self.grading_db, 'r', encoding='utf-8') as file:
            data = json.loads(f.readline())
            return data[name]

    def create_teacher(self):
        teacher = Teacher(self)
        return teacher


if __name__ == '__main__':
    admin = Administrator(['math', 'physics', 'bio'], ["a1"], "laptop")
    print(admin)
    print(admin.grades)
