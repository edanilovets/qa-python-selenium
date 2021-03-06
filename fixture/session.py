from selenium.common.exceptions import NoSuchElementException


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=submit]").click()
        try:
            wd.find_element_by_css_selector("#top b").text == "(%s)" % username
        except NoSuchElementException:
            return False
        return True

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

