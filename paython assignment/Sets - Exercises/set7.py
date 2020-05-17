#7. Write a Python program to create a union of sets.

set1=set(['A','B','C','D','E'])
set2=set(['T','U','D','Y'])
set3=set(['H','O','V','D','T'])


#set4= set1 | set2 | set3
#print(set4)

print("set1 U set2:",set1.union(set2))
print("set1 U set2 U set3:",set1.union(set2,set3))


