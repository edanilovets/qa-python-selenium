from model.group import Group


group_1 = Group(gid=1, name="group1", header="header1", footer="footer1")
group_2 = Group(gid=10, name="group2", header="header2", footer="footer2")
group_3 = Group(gid=13, name="group3", header="header3", footer="footer3")
group_4 = Group(gid=100, name="group3", header="header3", footer="footer3")
groups = [group_1, group_2, group_3, group_4]

# print(groups)
# groups[0:1] = []
# groups.pop(2)
# print(groups.count(group_1))
# groups.sort(key=lambda x: x.gid, reverse=True)
# print(groups)
#
# squares = [x**2 for x in range(10)]
# print(squares)

# Some tips
list_int = list(range(0, 100, 4))
print(list_int)

# Multiple assignment
cat = ['fat', 'orange', 'loud']
size, color, noise = cat
print(size)
print(color)
print(noise)

# Reverse lists
tab = [1, 2, 3]

tab = list(reversed(tab))
tab.reverse()
tab = tab[::-1]

# Questions
# How to select an element from list?
