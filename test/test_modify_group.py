"""
Application address book
Tests for modifying groups
"""

from model.group import Group
from random import randrange


def test_modify_random_group_name(app):
    group = Group(name="xx group#000")  # group data for input
    if app.group.count() == 0:
        app.group.create(
            Group(name="group#for_modify", header="group_header#for_modify", footer="group_footer#for_modify"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))  # group index for input
    group.gid = old_groups[index].gid
    app.group.modify_random_group(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    old_groups.sort(key=lambda x: int(x.gid), reverse=True)
    new_groups.sort(key=lambda x: int(x.gid), reverse=True)
    assert old_groups == new_groups
