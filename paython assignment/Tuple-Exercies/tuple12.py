#12. Write a Python program to remove an item from a tuple.


tup='a','b','c','w',3,6,4,'f','sdfv'
print(tup)

list1=list(tup)
list1.remove('b')
tup1=tuple(list1)
print(tup1)
             