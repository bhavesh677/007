def UP(n):
    lst = []

    for i in range(n):
        a = input()
        lst.append(a)
        
    for i in lst:
        print(i.upper())
    
n = int(input("Enter number of rows to be entered: "))

UP(n)
    



