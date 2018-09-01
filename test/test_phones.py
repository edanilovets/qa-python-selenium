"""
Application address book
Tests for contacts on home page
"""


def test_phones(app):
    contacts = app.contact.get_contacts_list()
    # todo: add test implementation here
    print(contacts)