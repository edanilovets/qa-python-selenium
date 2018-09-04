import pytest
from fixture.application import Application


@pytest.fixture(scope="session", autouse=True)
def app(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    fixture = Application(browser=browser, url=base_url)
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost:8080/addressbook/")
