#23. Write a Python program to flatten a shallow list

lst = [[2,4,3],[1,5,6], [9], [7,9,0]]

a=[]

for i in lst:
    for j in i:
        a.append(j)
        
print(a)




    
