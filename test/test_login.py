from app import login, register


def test_successful_login(cursor, random_user):
    username = random_user.name
    password = random_user.password
    email = random_user.email
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


def test_login_incorrect_password(cursor, random_user):
    username = random_user.name
    password = random_user.password
    password2 = password + "hi"
    email = random_user.email
    register(username, password, email)
    token = login(username, password2)
    assert token is None
    cursor.execute("DELETE FROM users WHERE name = %s;", (username,))




