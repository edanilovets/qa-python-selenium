import pytest
import json
import os.path
from fixture.application import Application
from fixture.db import DbFixture

target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as file:
            target = json.load(file)
    return target


@pytest.fixture(scope="session", autouse=True)
def app(request):
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    fixture = Application(browser=browser, url=web_config["baseUrl"])
    fixture.session.login(username=web_config["username"], password=web_config["password"])

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    db_fixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                           password=db_config['password'])

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture
