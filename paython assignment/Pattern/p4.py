n = int(input("Enter number of rows: "))

for i in range(n):
    
    print(" "*(n-1-i),end="")
    for p in range(1+i,0,-1):
        print(p,end=" ")
        
    print()
        
    


