#1. Write a Python program to sum all the items in a list. 


def sum_list(data):
    suml=0
    for i in data:
        suml+=i
    return suml
    
print(sum_list([2,3,4]))