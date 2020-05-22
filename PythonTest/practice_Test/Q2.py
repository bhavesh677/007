n = int(input("Enter number: "))

def Dtable(n):
    lst = []
    for i in range(1,n+1):
        lst.append([i,i*i])
        
    return dict(lst)

print(Dtable(n))


d = {}

for i in range(1,n+1):
    d[i] = i * i
    
print(d)
        


    



