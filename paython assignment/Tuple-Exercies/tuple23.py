#24. Write a Python program to count the elements in a list until an element is a tuple.


data= [[1,2,3,4],{3,4,5,6},"bhaves",(1,2,3,4),[4,5,6,7],"bhavesh"]
cnt = 0

'''

for i in data:
    if type(i) != tuple :
        cnt += 1
        
    else:
        break
        
print(cnt)


'''

for i in data:
    if isinstance(i, tuple):
        break
    
    cnt += 1

print(cnt)


        



