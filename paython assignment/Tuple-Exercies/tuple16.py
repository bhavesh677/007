#16. Write a Python program to convert a tuple to a dictionary.

tup=((1,'bhavesh'),(2,'abcdef'))
print(dict((x,y)for x,y in tup))