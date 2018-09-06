import copy

lst = [1, 2, 3]

lst1 = lst
lst2 = lst[:]
lst3 = copy.copy(lst)
lst4 = copy.deepcopy(lst)

lst[1] = 0

print("lst[1]: %s" % lst[1])
print("lst1[1]: %s" % lst1[1])
print("lst2[1]: %s" % lst2[1])
print("lst3[1]: %s" % lst3[1])
print("lst4[1]: %s" % lst4[1])

