#10. Write a Python program to issubset and issuperset. 

#issubset
'''
A = {1, 2, 3} 
B = {1, 2, 3, 4, 5} 
C = {1, 2, 4, 5} 

print(A.issubset(B)) #TRUE
print(B.issubset(C)) #FALSE
print(C.issubset(B))  #TRUE
'''

#issuperset

A = {1, 2, 3} 
B = {1, 2, 3, 4, 5} 
C = {1, 2, 4, 5}

print(A.issuperset(B)) #FALSE
print(B.issuperset(C)) #TRUE
print(B.issuperset(A)) #TRUE