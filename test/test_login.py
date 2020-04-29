from app import login, register
from fixtures import cursor


def test_successful_login(cursor):
    username = "noah"
    password = "animalc"
    email = "fa;sdkl@"
    register(username, password, email)
    token = login(username, password)
    cursor.execute("""SELECT token
        FROM tokens
            JOIN users ON tokens.user_id = users.id
        WHERE users.name = %s;""", (username,))
    rec = cursor.fetchone()
    assert rec["token"] == token
    cursor.execute("DELETE FROM tokens WHERE token = %s;", (token,))
    cursor.execute("DELETE FROM users WHERE name = %s;", (username,))


def test_login_incorrect_password(cursor):
    username = "noah"
    password = "animalc"
    password2 = "askdlfj"
    email = "fa;sdkl@"
    register(username, password, email)
    token = login(username, password2)
    assert token is None
    cursor.execute("DELETE FROM users WHERE name = %s;", (username,))




