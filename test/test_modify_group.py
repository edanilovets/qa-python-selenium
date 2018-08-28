"""
Application address book
Tests for modifying groups
"""

from model.group import Group


def test_modify_first_group_name(app):
    group = Group(name="xx group#000")
    old_groups = app.group.get_group_list()
    group.gid = old_groups[0].gid
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    old_groups.sort(key=lambda x: int(x.gid), reverse=True)
    new_groups.sort(key=lambda x: int(x.gid), reverse=True)
    assert old_groups == new_groups


def test_modify_first_group_name_header(app):
    group = Group(name="zz header#001", header="xx header#000")
    old_groups = app.group.get_group_list()
    group.gid = old_groups[0].gid
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    old_groups.sort(key=lambda x: int(x.gid), reverse=True)
    new_groups.sort(key=lambda x: int(x.gid), reverse=True)
    print()
    print(old_groups)
    print(new_groups)
    assert old_groups == new_groups


def test_modify_first_group_name_header_footer(app):
    group = Group(name="zz header#001", header="xx header#000", footer="footer##new")
    old_groups = app.group.get_group_list()
    group.gid = old_groups[0].gid
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    old_groups.sort(key=lambda x: int(x.gid), reverse=True)
    new_groups.sort(key=lambda x: int(x.gid), reverse=True)
    print()
    print(old_groups)
    print(new_groups)
    assert old_groups == new_groups