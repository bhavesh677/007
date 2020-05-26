#3.Write a Python program for Binary search.


data = [9,8,7,6,5,4,3,2,1,10]

sdata = sorted(data)


l = 0 
u = len(data) - 1
flag = 0
n = int(input("Enter number: "))


while(l <= u):
    m = (l+u)//2
    if(n > sdata[m]):
        l = m +1
    elif (n < sdata[m]):
        u = m - 1
    else:
        flag = 1
        for i in range(len(data)):
            if i == n:
                print("number found at %d index"%(i))
            
        break

if flag == 1:
    print("Number found")
else:
    print("Not found")
    

    
