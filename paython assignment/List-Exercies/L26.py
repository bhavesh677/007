#27. Write a Python program to find the second smallest number in a list. 

def secondsmall(lst):
    if (len(lst) < 2):
        return
    elif (len(lst) == 2 and lst[0] == lst[1]):
        return 
    elif (len(lst) < 2):
        return 
    else:
        sort=sorted(lst)
        unq=set(sort)
        fnl=list(unq)
        dn=sorted(fnl)
        return dn[1]
    
lst=[2,2]
print(secondsmall(lst))

    
