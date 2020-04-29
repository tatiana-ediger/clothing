from flask import Flask, request, jsonify
import psycopg2

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


if __name__ == '__main__':
    app.run()
