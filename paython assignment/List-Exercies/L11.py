#11. Write a Python function that takes two lists and returns True if they
#have at least one common member. 

def one(data1,data2):
    result=False
    for i in data1:
        for j in data2:
            if i == j:
                result=True
    return result
    
print(one([1,2,3,4],[2,6,7,8,9,10]))
print(one([1,2,3,4],(5,6,7,8,9)))