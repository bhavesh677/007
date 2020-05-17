#4. Write a Python program to remove item(s) from set 

myset=set(['bhavesh','vita','007','dbda'])
print(myset)

myset.pop()
print(myset)
myset.pop()
print(myset)

#to remove element from the set if it is there in the set

myset.discard('bhavesh')
print(myset)


