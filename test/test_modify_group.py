"""
Application address book
Tests for modifying groups
"""

from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="z group#000"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="z header#000"))
