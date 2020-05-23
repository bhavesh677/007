def AS(n):
    lst = []
    
    for i in range(1,n+1):
        lst.append(i)
        
    s = ""
    for i in lst:
        s += str(i) + " + "
        
    
    sf = s[:-2]
    return "%s= %d" %(sf,sum(lst))
    
    
        
n = int(input("Enter number: "))        
print(AS(n))

