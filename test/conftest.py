import string
from dataclasses import dataclass
import random

import pytest
import psycopg2
import psycopg2.extras

from app import register, login


@pytest.fixture
def cursor():
    conn = psycopg2.connect("dbname=postgres")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    yield cur
    conn.commit()
    cur.close()
    conn.close()


@pytest.fixture
def valid_token(cursor, random_user):
    register(random_user.name, random_user.password, random_user.email)
    token = login(random_user.name, random_user.password)
    yield token
    cursor.execute("DELETE FROM tokens WHERE token = %s;", (token,))
    cursor.execute("DELETE FROM users WHERE name = %s;", (random_user.name,))


@pytest.fixture
def valid_user_id(cursor, random_user):
    register(random_user.name, random_user.password, random_user.email)
    cursor.execute("SELECT id FROM users WHERE name = %s", (random_user.name,))
    yield cursor.fetchone()["id"]
    cursor.execute("DELETE FROM users WHERE name = %s;", (random_user.name,))


@dataclass
class User:
    name: str
    password: str
    email: str


@pytest.fixture
def random_user():
    def generate_string():
        return str(random.choices(string.printable, k=random.randint(2,20)))
    return User(generate_string(), generate_string(), generate_string())
