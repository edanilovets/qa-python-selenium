"""
Application address book
Tests for adding groups
"""
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="group#1", header="group_header#1", footer="group_footer#1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
