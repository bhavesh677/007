#Write a Python program to pack consecutive duplicates of a given list elements into sublists. 
##Original list:[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
##After packing consecutive duplicates of the said list elements into sublists:
##[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

data = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

sdata = sorted(data)

print(sdata)

lst = []

for i in sdata:
    if [i] not in lst:
        lst.append([])
        lst[i].append(i)
    
    else :
        lst[i].append(i)
        
        
flst = [i for i in lst if i != []]

print(flst)
        
        
        
    
    
        
    


