import pytest
import json
import os.path
from fixture.application import Application

target = None


@pytest.fixture(scope="session", autouse=True)
def app(request):
    browser = request.config.getoption("--browser")
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
    global target
    if target is None:
        with open(config_file) as file:
            target = json.load(file)

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
