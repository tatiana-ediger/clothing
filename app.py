from datetime import datetime

from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras
from uuid import uuid4

app = Flask(__name__)


@app.route('/register', methods=["POST"])
def handle_register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    email = data["email"]
    register(username, password, email)
    return "OK"


def register(username, password, email):
    conn = psycopg2.connect("dbname=postgres")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("INSERT INTO users (name, password, email) VALUES (%s, %s, %s)",
                (username, password, email))
    conn.commit()
    cur.close()
    conn.close()


@app.route('/login', methods=["POST"])
def handle_login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    token = login(username, password)
    return token


def login(username, password):
    conn = psycopg2.connect("dbname=postgres")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT id from users WHERE users.name = %s AND users.password = %s", (username,password))
    rec = cur.fetchone()
    if rec is None:
        return None
    user_id = rec["id"]
    token = str(uuid4())
    exp_date = datetime.now()
    cur.execute("INSERT INTO tokens (user_id, token, exp_date) VALUES (%s, %s, %s)",
                (user_id, token, exp_date))
    conn.commit()
    cur.close()
    conn.close()
    return token


if __name__ == '__main__':
    app.run()
