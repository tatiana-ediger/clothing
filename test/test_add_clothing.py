from app import add_clothing, register


def test_add_clothing(cursor, valid_user_id):
    user_id = valid_user_id

    clothing_name = "shirt"
    color = "white"
    add_clothing(user_id, clothing_name, color)
    cursor.execute("SELECT * FROM clothing WHERE user_id = %s;", (user_id,))
    clothing_rec = cursor.fetchone()

    assert clothing_rec["name"] == clothing_name
    assert clothing_rec["color"] == color

    cursor.execute("DELETE FROM clothing WHERE user_id = %s;", (user_id,))


