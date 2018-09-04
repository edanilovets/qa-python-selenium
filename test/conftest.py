import pytest
from fixture.application import Application


@pytest.fixture(scope="session", autouse=True)
def app(request):
    fixture = Application(browser="firefox")
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
