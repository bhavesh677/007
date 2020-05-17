#13. Write a Python program to slice a tuple.

tup=('a', 'b', 'c', 'w', 3, 6, 4, 'f', 'sdfv')

tup1= tup[3:7]
print(tup1)

tup2= tup[5:]
print(tup2)

tup3= tup[:7]
print(tup3)

tup4= tup[:]
print(tup4)

tup5=tup[0:9:2] #start:stop:steps
print(tup5)

