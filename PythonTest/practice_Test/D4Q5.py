'''5.Write a Python function that takes a list and returns a new list 
with unique elements of the first list.
Sample List : [11,22,22,33,33,33,44,55,55,66]
Unique List : [11, 22,33, 44, 55,66]
'''

def UNQ(data):
    return set(data)

data = [11,22,22,33,33,33,44,55,55,66]

print(sorted(UNQ(data)))

