"""
Application address book
Tests for adding groups
"""
from model.group import Group


def test_add_group(app):
    group = Group(gid="1000", name="group#1", header="group_header#1", footer="group_footer#1")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    old_groups.sort(key=lambda x: int(x.gid), reverse=True)
    new_groups.sort(key=lambda x: int(x.gid), reverse=True)
    assert old_groups == new_groups


def test_add_empty_group(app):
    group = Group(gid="1000", name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    old_groups.sort(key=lambda x: int(x.gid), reverse=True)
    new_groups.sort(key=lambda x: int(x.gid), reverse=True)
    assert old_groups == new_groups
