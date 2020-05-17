#How to create a series from a list, numpy array and dict?
import pandas as pd
import numpy as np

#:Create a series from array without index.
'''
data=np.array(['bhavesh','mohan','sawant'])
print(data,type(data))

s=pd.Series(data)
print(s,type(s))
'''

#Create a series from array with index.
'''
data=np.array(['bhavesh','mohan','sawant'])
print(data,type(data))

s=pd.Series(data,index=[5,6,7])
print(s,type(s))
'''

#Creating a Pandas Series from Dictionary

#Dictionary keys are given in sorted order
'''
dictionary={'A':10,'B':20,'C':30}
print(dictionary,type(dictionary))

s=pd.Series(dictionary)
print(s,type(s))
'''

#Dictionary keys are given in unsorted order
'''
dictionary={'B':10,'A':20,'C':30}
print(dictionary,type(dictionary))

s=pd.Series(dictionary)
print(s,type(s))
'''

# Index list is passed of same length as the number of keys present in dictionary
'''
dictionary={'B':10,'A':20,'C':30}
print(dictionary,type(dictionary))

s=pd.Series(dictionary,index=['A','B','C'])
print(s,type(s))
'''

#Index list is passed of greater length than the number of keys present in dictionary in this case, Index order is persisted and the missing element is filled with NaN (Not a Number).
'''
dictionary={'B':10,'A':20,'C':30}
print(dictionary,type(dictionary))

s=pd.Series(dictionary,index=['A','B','C','D'])
print(s,type(s))
'''

#Creating a Pandas Series from Lists
'''
data=['bhavesh','abhishek','sanyukta','yash']
print(data,type(data))

s=pd.Series(data)
print(s,type(s))
'''

data=['bhavesh','abhishek','sanyukta','yash']
print(data,type(data))

s=pd.Series(data,index=[2,4,6,8])
print(s,type(s))


















