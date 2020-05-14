l1 = []
n = int(input("Enter number of elements for list1 : "))
for i in range(0, n): 
    element = int(input()) 
    l1.append(element)
l2 = []
n = int(input("Enter number of elements for list2: "))
for i in range(0, n): 
    element = int(input()) 
    l2.append(element)    
new = list()

Odd = l1[1::2]
print("Element at odd index positions from list1: ",Odd)

Even = l2[0::2]
print("Element at Even index positions from list2: ",Even)

print("Mixed list with odd even index positions")
new.extend(Odd)
new.extend(Even)
print(new)