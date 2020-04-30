import json

from app import register, app


def test_register(cursor, random_user):
    username = random_user.name
    password = random_user.password
    email = random_user.email
    register(username, password, email)
    cursor.execute("SELECT * FROM users WHERE name = %s;", (username,))
    rec = cursor.fetchone()
    assert username == rec["name"]
    assert password == rec["password"]
    assert email == rec["email"]
    cursor.execute("DELETE FROM users WHERE name = %s;", (username,))


def test_handle_register(cursor):
    username = "greg"
    password = "23456"
    email = "gr@galk;sjdf"
    app.testing = True
    client = app.test_client()
    resp = client.post("/register", data=json.dumps({
        "username": username,
        "password": password,
        "email": email,
    }), follow_redirects=True, content_type='application/json')
    assert resp.status_code == 200
    cursor.execute("SELECT * FROM users WHERE name = %s;", (username,))
    rec = cursor.fetchone()
    assert username == rec["name"]
    assert password == rec["password"]
    assert email == rec["email"]
    cursor.execute("DELETE FROM users WHERE name = %s;", (username,))
