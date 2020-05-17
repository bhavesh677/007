#5. Write a Python program to add an item in a tuple.


tup=('bhavesh', '007', 'DBDA', 'VITA')

tup = tup + ("Andheri",)
print(tup)


#adding items in a specific index

tup = tup[:2] + (2,4,5) + tup[:2]

print(tup)


#converting the tuple to list

l=list(tup)

l.append(30)

tup=tuple(l)
print(tup)