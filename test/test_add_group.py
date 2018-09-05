"""
Application address book
Tests for adding groups
"""
import pytest
from data.add_group import constant_data as test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    old_groups.sort(key=lambda x: int(x.gid), reverse=True)
    new_groups.sort(key=lambda x: int(x.gid), reverse=True)
    # print(old_groups)
    # print(new_groups)
    assert old_groups == new_groups
