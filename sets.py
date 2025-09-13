#sets are unodered items that cannot be changed but can be removed or added.
#they do not allow duplicates
'''
my_set = {3,4,2,1}

print(my_set, "\n")

my_set.add(0)
print(my_set, "\n")

my_set.remove(2)
print(my_set, "\n")

'''

my_set = {3,4,2,1}
my_set1 = {4,7,8,5}

my_union = my_set.union(my_set1) #union combines the sets into one set with no duplicates
print(my_union, "\n")

#intersection is an item that is common or the same in various sets

interset = my_set.intersection(my_set1)
print(interset, "\n")