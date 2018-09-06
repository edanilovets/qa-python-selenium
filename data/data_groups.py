import random
import string

from model.group import Group


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    # symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


# Constant test data
constant_data = [
    Group(gid="900", name="name_1", header="header_1", footer="footer_1"),
    Group(gid="900", name="name_2", header="header_2", footer="footer_2")
]

# Test data with 1 empty group and 5 randomly created
generated_data_1 = [Group(gid="900", name="", header="", footer="")] + [
    Group(gid="900", name=random_string("name_", 20), header=random_string("header_", 50),
          footer=random_string("footer_", 50))
    for i in range(5)
]

# Test data using list comprehension: 8 combinations of empty string and random data
generated_data_2 = [
    Group(gid="900", name=name, header=header, footer=footer)
    for name in ["", random_string("name_", 20)]
    for header in ["", random_string("header_", 50)]
    for footer in ["", random_string("footer_", 50)]
]
