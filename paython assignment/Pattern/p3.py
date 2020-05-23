n = int(input("Enter number of rows: "))
a = 1

for i in range(n):
    print(" "*(n-i-1),end="")
    
    for p in range(1,i+2):
          print(a, end=' ')
          a += 1
          
        
    print()
  

