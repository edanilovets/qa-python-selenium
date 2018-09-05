"""
Application address book
Tests for adding groups
"""
import pytest
import random
import string

from model.group import Group


def random_string(prefix, max_len):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


# Test data with 1 empty group and 5 randomly created
test_data_1 = [Group(gid="900", name="", header="", footer="")] + [
    Group(gid="900", name=random_string("name_", 20), header=random_string("header_", 50),
          footer=random_string("footer_", 50))
    for i in range(5)
]

# Test data using list comprehension: 8 combinations of empty string and random data
test_data_2 = [
    Group(gid="900", name=name, header=header, footer=footer)
    for name in ["", random_string("name_", 20)]
    for header in ["", random_string("header_", 50)]
    for footer in ["", random_string("footer_", 50)]
]


@pytest.mark.parametrize("group", test_data_1, ids=[repr(x) for x in test_data_1])
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
