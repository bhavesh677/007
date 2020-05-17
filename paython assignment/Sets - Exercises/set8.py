#8. Write a Python program to create set difference

set1=set(['A','B','C','D','E'])
set2=set(['T','U','D','Y'])
set3=set(['H','O','V','D','T'])

'''set4=set1 - set2
print(set4)

set5=set2-set1
print(set5)'''


print(set1.difference(set2))
print(set1.difference(set2,set3))

