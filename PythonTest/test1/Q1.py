#Count the total number of digits in a number
def count(n):
    cnt=0
    while n != 0:
        n = n // 10
        cnt = cnt + 1
    
    return cnt

number=int(input("Enter a number: "))

x=count(number)

print("Number of digits in %d are %d"%(number,x))


#Reverse the following list using for loop

def reverse(lst):
    rlst=[]
    for i in range(1,len(lst)+1):
        rlst.append(lst[len(lst)-i])
        
    return rlst


lst=[]

n=int(input("enter number of elements in the list: "))

for i in range(n):
    a=int(input())
    lst.append(a)
    
print(lst)

print("reverse list is: ",reverse(lst))

