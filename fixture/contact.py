from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def get_contacts_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []   # list of contacts objects
        lines = wd.find_elements_by_css_selector("tr[name=entry]")
        for i in range(len(lines)):
            contact = Contact()
            contact.cid = lines[i].find_elements_by_tag_name("td")[0].find_element_by_tag_name("input")\
                .get_attribute("value")
            contact.last_name = lines[i].find_elements_by_tag_name("td")[1].text
            contact.first_name = lines[i].find_elements_by_tag_name("td")[2].text
            contact.all_phones = lines[i].find_elements_by_tag_name("td")[5].text
            contacts.append(contact)
        return contacts
