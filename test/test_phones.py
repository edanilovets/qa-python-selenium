"""
Application address book
Tests for contacts on home page
"""
import re


def test_phones(app):
    first_contact_home = app.contact.get_contacts_list()[0]
    first_contact_form = app.contact.get_contacts_from_edit_page()[0]

    def clear(s):
        return re.sub('[() -]', '', s)

    phones_1 = first_contact_home.all_phones.splitlines()
    phones_2 = [clear(first_contact_form.home_phone), clear(first_contact_form.mobile_phone),
                clear(first_contact_form.work_phone)]
    assert phones_1 == phones_2
