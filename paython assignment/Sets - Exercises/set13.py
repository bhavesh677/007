#13. Write a Python program to use of frozensets
set1 = frozenset([1, 2, 3, 4, 5])
set2 = frozenset([6, 7, 8, 1,2 ])
#use isdisjoint(). Return True if the set has no elements in common with other. 
print(set1.isdisjoint(set2))
#use difference(). Return a new set with elements in the set that are not in the others.
print(set1.difference(set2))
#new set with elements from both x and y
print(set1 | set2)

#set1.pop() this will give error

#set1.add('bhaveshj') this will give error