from model.group import Group

groups = []
group_1 = Group(gid=1, name="group1", header="header1", footer="footer1")
group_2 = Group(gid=10, name="group2", header="header2", footer="footer2")
group_3 = Group(gid=13, name="group3", header="header3", footer="footer3")
group_4 = Group(gid=100, name="group3", header="header3", footer="footer3")

groups.append(group_1)
groups.append(group_2)
groups.append(group_3)
groups.append(group_1)
groups.append(group_4)

# print(groups)
# groups[0:1] = []
# groups.pop(2)
# print(groups.count(group_1))
# groups.sort(key=lambda x: x.gid, reverse=True)
# print(groups)
#
# squares = [x**2 for x in range(10)]
# print(squares)

# Questions
# How to select an element from list?
print(groups)
print("Index 1: %s" % groups[1])
print("Last: %s" % groups[-1])
