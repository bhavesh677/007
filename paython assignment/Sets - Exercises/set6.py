#6. Write a Python program to create an intersection of sets

set1=set(['bhavesh','abhishek','joshua','yash'])
set2=set(['sagar','kavita','sameer','yash','ravi'])
set3=set(['dhiraj','kavita','bhavesh','yash','abhishek'])

set4=set1 & set2
print(set4)

print(set1.intersection(set2))
print(set1.intersection(set3))
print(set2.intersection(set3))
print(set1.intersection(set2,set3))