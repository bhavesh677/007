#12. Write a Python program to print a specified list after removing the 0th, 4th
#and 5th elements

#method 1
'''
def remove(data):
    newlist=[]
    for i in range(len(data)):
        if i != 0 and i != 4 and i !=5:
            newlist.append(data[i])
    return newlist

mylist=[1,2,3,4,5,6,7,8,9,10]

print(remove(mylist))
'''

#method 2
'''
def remove1(data):
    data.pop(0)
    return data

m1=[1,2,3,4,5,6,7,8,9,10]

print(remove1(m1))
'''

#method 3

mylist=[1,2,3,4,5,6,7,8,9,10]
mylist=[x for (i,x) in enumerate(mylist) if i not in (0,4,5)]
print(mylist)