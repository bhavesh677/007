#9. Write a Python program to create a symmetric difference


set1=set(['A','B','C','D','E'])
set2=set(['A','C','D','Y'])
set3=set(['H','Y','V','D','E'])


#set4=set1 ^ set2
#print(set4)


print(set1.symmetric_difference(set2))
print(set1.symmetric_difference(set3))