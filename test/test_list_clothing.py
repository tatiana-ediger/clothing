from app import add_clothing, list_clothing


def test_list_clothing(valid_user_id, cursor):
    assert list_clothing(valid_user_id) == []
    name1 = "jeans"
    color1 = "blue"
    add_clothing(valid_user_id, name1, color1)
    assert list_clothing(valid_user_id) == [{"name": name1, "color": color1}]
    name2 = "shirt"
    color2 = "white"
    add_clothing(valid_user_id, name2, color2)
    expected = [{"name": name1, "color": color1}, {"name": name2, "color": color2}]
    assert list_clothing(valid_user_id) == expected
    cursor.execute("DELETE FROM clothing WHERE user_id = %s", (valid_user_id,))
