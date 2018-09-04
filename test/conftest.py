import pytest
import json
from fixture.application import Application

target = None


@pytest.fixture(scope="session", autouse=True)
def app(request):
    browser = request.config.getoption("--browser")
    global target
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)

    fixture = Application(browser=browser, url=target["baseUrl"])
    fixture.session.login(username=target["username"], password=target["password"])

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
