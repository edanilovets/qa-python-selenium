"""
Application address book
Tests for deletion groups
"""
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group#for_del", header="group_header#for_del", footer="group_footer#for_del"))
    app.group.delete_first_group()
