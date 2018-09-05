import random
import string
import os
import json
from model.group import Group


def random_string(prefix, max_len):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    f.write(json.dumps(generated_data_1, default=lambda x: x.__dict__, indent=2))
