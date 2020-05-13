def mean(mylist):
    the_mean=sum(mylist)/len(mylist)
    return the_mean

lst=[]
n=int(input("enter no. of elements:"))

for i in range(0,n):
    a=int(input())
    lst.append(a)
    
print(lst)
print(mean(lst))
























