def table(n):
    for i in range(1,11):
        p = n * i
        print("%d * %d = %d"%(n,i,p))
        
n = int(input("Enter number: "))
table(n)
        
