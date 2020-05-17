#5. Write a Python program to remove an item from a set if it is present in the set. 

myset=set(['1','3','5','8','9'])
print(myset)

a=input("enter an element which you want to remove from the set:")
myset.discard(a)
print(myset)
