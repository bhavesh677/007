#9. Write a Python program to clone or copy a list. 

#method 1
'''
list1=[1,2,3,46,5,8,7]

def copy_list(data):
    copy=data[:]
    return copy

print(copy_list(list1))
'''

#method 2

list1=[1,2,3,5,8,7]

def copy_list_ex(data):
    copy=[]
    copy.append(data)
    return copy

print(copy_list_ex(list1))


#method 3
'''
def copy(data):
    copy=list(data)
    return copy

list1=[1,2,3,5,8,7]

print(copy(list1))
'''