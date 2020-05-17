#3. Write a Python program to get the largest number from a list. 


def max_num(data):
    max=data[0]
    for i in data:
        if i > max:
            max=i
    return max
        
print(max_num([0,-4,-6,-8,-9]))