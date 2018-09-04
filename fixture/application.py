from selenium import webdriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class Application:

    def __init__(self, browser):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            self.wd = webdriver.Firefox(firefox_binary=binary)
        elif browser == "edge":
            self.wd = webdriver.Edge()

        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def destroy(self):
        self.wd.quit()
