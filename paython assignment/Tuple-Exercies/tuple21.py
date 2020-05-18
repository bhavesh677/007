'''22. Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']'''


#method 1

'''
def Rempty(data):
    lst=[]
    for i in data:
        if (i != ()):
            lst.append(i)
    return lst


data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(Rempty(data))
'''

# best method 

data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

new = [i for i in data if i]

print(new)




