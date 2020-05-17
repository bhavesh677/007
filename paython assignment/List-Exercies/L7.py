#7. Write a Python program to remove duplicates from a list. 




'''#method 1
mylist=[10,20,45,67,10,20,45,67,67]
print("my data with duplicate enrties:",mylist)

myset=set(mylist)
print("my data with unique entries:",myset)'''


#method 2
data=[10,10,20,45,67,10,20,45,67,67]

unique_items=[]

for i in data:
    if i  not in unique_items:
        unique_items.append(i)
        
        
print(unique_items)
