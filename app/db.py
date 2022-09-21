from surrealdb import AuthenticationError, QueryError, AsyncSurrealDB
import asyncio

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DB(metaclass=Singleton):
    _instance = None
    client = None

    def __init__(self, username, password, namespace, database, host, port):
        self.client = AsyncSurrealDB(username=username,
                                 password=password,
                                 namespace=namespace,
                                 database=database,
                                 url=f"http://{host}:{port}/sql"
                                )

    async def info_db(self) -> dict:
        response = await self.client.query("INFO FOR DB;")
        return response

    async def create(self, table, key="", **kwargs) -> dict:
        if key:
            table += ":" + key

        response = await self.client.create(table, **kwargs)
        return response

    async def query(self, stmt: str) -> dict:
        response = await self.client.query(stmt)
        return response

    async def update(self, table_key, **kwargs) -> dict:
        response = await self.client.change(table_key, **kwargs)
        return response

    async def delete(self, table, key="", **kwargs) -> dict:
        if key:
            table += ":" + key

        response = await self.client.delete(table, **kwargs)
        return response


async def db_grade_student(student_name, course, grade):
    db = DB()
    stmt = f"SELECT * FROM students WHERE name='{student_name}';"
    response = await db.query(stmt)

    # create student
    if len(response) == 0:
        courses = [{"course": course, "grade": grade}]
        return await db.create("students", name=student_name, courses=courses)

    student = response[0]
    idx = next((idx for idx in range(len(student['courses']))
                if student['courses'][idx]['course'] == course), None)

    # create course and grade
    if idx is None:
        student['courses'].append({"course": course, "grade": grade})
        return await db.update(student['id'], courses=student['courses'])

    # update course with grade
    student['courses'][idx]["grade"] = grade
    return await db.update(student['id'], courses=student['courses'])
