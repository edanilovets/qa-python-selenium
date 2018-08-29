"""
Application address book
Tests for deletion groups
"""
from model.group import Group
from random import randrange


def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group#for_del", header="group_header#for_del", footer="group_footer#for_del"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_random_group(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index + 1] = []
    assert old_groups == new_groups
