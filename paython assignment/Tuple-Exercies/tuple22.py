'''23. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]'''


def last(x):
    return x[-1]

def sort(data):
    return sorted(data,key=last,reverse = True)

data =[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sort(data))




