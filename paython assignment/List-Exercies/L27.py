#28. Write a Python program to find the second largest number in a list

def secondsmall(lst):
    if (len(lst) < 2):
        return
    elif (len(lst) == 2 and lst[0] == lst[1]):
        return 
    elif (len(lst) < 2):
        return 
    else:
        unq=set(lst) #this will give unique value
        fnl=sorted(unq) #this will sort those value in ascending order
        print(fnl)
        return fnl[-2]
    
lst=[1, 1, 1, 0, 0, 0, 2, -2, -2]
print(secondsmall(lst))

    
