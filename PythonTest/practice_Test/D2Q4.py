def Rsum(n):
    lst = []
    for l in range(n):
        lst.append([])
    
        
    a = 1
    for i in range (n):
        for p in range(1,i+2):
            lst[i].append(a)
            a += 2
            
    return sum(lst[n-1]),lst


n = int(input("Enter Row Number: "))    

s,L=Rsum(n)

print(L)


print("Sum of this row--> %s is--> %d"%(L[n-1],s))


            

