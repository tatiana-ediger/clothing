import pytest
import psycopg2
import psycopg2.extras


@pytest.fixture
def cursor():
    conn = psycopg2.connect("dbname=postgres")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    yield cur
    conn.commit()
    cur.close()
    conn.close()