#4. Write a Python program to get the smallest number from a list


def min_num(data):
    min=data[0]
    for i in data:
        if i < min:
            min=i
    return min

print(min_num([1,2,3,4,-5,0]))