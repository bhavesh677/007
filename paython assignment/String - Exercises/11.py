''' 11. Write a Python program to remove the characters which have odd index values
of a given string. '''

data = input("Enter string: ")

l = len(data)

ndata = ""

for i in range(0,l,2):
    
    ndata = ndata + data[i]
    
print(ndata)
    


