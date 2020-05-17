#30. Write a Python program to get the frequency of the elements in a list.

import collections

lst=[10,10,10,10,20,20,20,20,40,40,50,50,30]

cnt=collections.Counter(lst)

print(cnt)
 
    
