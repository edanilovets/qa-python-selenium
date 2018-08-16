import unittest
from selenium.webdriver.chrome.webdriver import WebDriver



class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicity_wait(60)


