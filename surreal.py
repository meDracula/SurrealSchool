import asyncio
from surrealdb import SurrealDB
from surrealdb import AuthenticationError, QueryError, AsyncSurrealDB

def test_init_db():
    with SurrealDB() as db:
        db.signin(username="root", password="root")
        db.use(namespace="test", database="test")
        result = db.query("INFO FOR DB;")
        print(result)

def init_db():
    client = AsyncSurrealDB(
        username="root",
        password="root",
        namespace="test",
        database="test",
        url="http://localhost:8000/sql",
    )
    return client

async def info_query(client):
        response = await client.query("SELECT * FROM author")
        print(response)


if __name__ == '__main__':
    client = init_db()
    asyncio.run(info_query(client))
