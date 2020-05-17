#19. Write a Python program to get the difference between the two lists.

l1=[5,6,7,8,4]
l2=[1,2,3,4,3,5]


c = list(set(l1) - set(l2))

print(c)




print(list(set(l1).difference(set(l2))))

    



