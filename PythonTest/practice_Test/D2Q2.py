def CEO(data):
    E,O = 0,0
    for i in data:
        if i % 2 == 0:
            E += 1
        else:
            O += 1
            
    return E,O

data = []

n = int(input("Enter Number of element: "))

for i in range(n):
    data.append(int(input()))
    


E,O=CEO(data)

print("In this list-->%s, Even count: %d and Odd count: %d"%(data,E,O))
        
