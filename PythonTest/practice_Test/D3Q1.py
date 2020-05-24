'''1.You are given with a list of integer elements. Make a new list which will store
square of elements of previous list.'''

def LSQR(lst):
    SQRlst = [i**2 for i in lst]
    return SQRlst

n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    lst.append(int(input()))
    
print("Square of entered list:",LSQR(lst))
