#2.Write a Python program for sequential search (Linear search).

lst = [1,2,3,4,5,6]

n = int(input("Enter number: "))

flag = 0

for i in range(len(lst)):
    if lst[i] == n:
        
        print("number found at index %d"%(i))
        flag = 1
        
if flag == 0:
    print("number not found")

    

