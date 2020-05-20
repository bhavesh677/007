'''8. Write a Python function that takes a list of words and
 returns the length of the longest one. '''
 
lst = ["bhavesh","sawant","vita","vidyanidhi"]

length = [len(i) for i in lst]

m = max(length)

mxw = [i for i in lst if len(i) == m]

print("longest word is %s with length: %d" %(mxw[0],m))





