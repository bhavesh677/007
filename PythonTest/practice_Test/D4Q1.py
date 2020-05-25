#1.	Write a function to find max of three numbers.

def Max(data):
    if data[0] > data[1] and data[0] > data[2]:
        return data[0]
    elif data[1] > data[2]:
        return data[1]
    else:
        return data[2]
    
lst = []    
    
for i in range(3):
    lst.append(int(input("--> ")))
    
print("Max of three numbers is: ",Max(lst))
