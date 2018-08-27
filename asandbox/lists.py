from model.group import Group

groups = []
group_1 = Group(gid=1, name="group1", header="header1", footer="footer1")
group_2 = Group(gid=10, name="group2", header="header2", footer="footer2")
group_3 = Group(gid=13, name="group3", header="header3", footer="footer3")

groups.append(group_1)
groups.append(group_2)
groups.append(group_3)

print(groups)
groups[0:1] = []
print(groups)
