from dotenv import load_dotenv
from settings import ENV
from db import DB, db_grade_student
import asyncio

from administrator import Administrator
from teacher import Teacher


def create_app():
    env = ENV()
    db = DB(*env.db_get())
    #print(asyncio.run(db.info_db()))

    #courses = [{"course": "database", "grade": "A"}]
    #print(asyncio.run(db.create("students", name="john doe", courses=courses)))

    #courses = [{"course": "math", "grade": "E"}]
    #print(asyncio.run(db.create("students", name="john ripper", courses=courses)))

    #asyncio.run(db.delete("students", where="name = 'john doe'"))
    #resp = asyncio.run(db_grade_student("john doe", "math", "C"))

    #resp = asyncio.run(db_grade_student("joe danger", "math", "B"))
    #print(resp)


if __name__ == '__main__':
    load_dotenv()
    create_app()
    #admin = Administrator(['math', 'physics', 'bio'], ["a1"], "laptop")
    #teacher = admin.create_teacher()
    #teacher.set_student_grade("steve", "math", "A")
