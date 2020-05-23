n = int(input("Enter number of rows: "))

for i in range(n):
    print((" "*(n-1-i))+(str(i+1)+" ")*(i+1))