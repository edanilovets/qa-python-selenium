import pytest


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return "%s:%s" % (self.username, self.password)


# Test data
test_data = [
    User(username="", password=""),
    User(username="admin", password="secret"),
    User(username="admin", password=""),
    User(username="", password="secret"),
    User(username="admin", password="secret"),
    User(username="john", password="secret")
]


@pytest.mark.parametrize("user", test_data, ids=[repr(x) for x in test_data])
def test_login(app, user):
    login_status = app.session.login(username=user.username, password=user.password)
    assert login_status
    if login_status:
        app.session.logout()


