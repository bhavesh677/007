'''16. Write a Python program to generate and print a list of first and last 5 elements where the
values are square of numbers between 1 and 30 (both included).'''


l=[]

for i in range(1,31):
    l.append(i**2)
    
print("Square of first five: ",l[0:5])
print("Square of last five: ",l[-5:])


