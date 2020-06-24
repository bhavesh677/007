'''Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]'''

data = [0,1,2,3,4,5,6,7]
new = data.copy()

for i in range (0,len(data),2):
    new[i],new[i+1] = data[i+1],data[i]
print(new)

new1 = [data[i+1] if i%2 == 0 else data[i-1] for i in range(0,len(data))]
print(new1)