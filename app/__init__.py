from dotenv import load_dotenv
from settings import ENV
from db import DB
import asyncio


def create_app():
    env = ENV()

    DB(*env.db_get())
    asyncio.run(DB.test_db())


create_app()
