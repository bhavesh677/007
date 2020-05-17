#2. Write a Python program to multiplies all the items in a list

def mul_list(data):
    mul=1
    for i in data:
        mul*=i
    return mul

print(mul_list([2,3,5]))
