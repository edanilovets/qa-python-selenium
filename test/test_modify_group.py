"""
Application address book
Tests for modifying groups
"""

from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="z group#000"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="z header#000"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
