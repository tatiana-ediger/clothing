from app import authenticate


def test_authenticate_fail():
    assert authenticate("jkdlsjfka") is None


def test_authenticate_succeed(valid_token, valid_user_id):
    assert authenticate(valid_token) == valid_user_id
