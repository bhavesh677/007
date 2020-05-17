#from list to array
import numpy as np
'''
data=[1,2,3,4,5,6,7,8,9]
data=np.array(data)
data=data.reshape(3,3)
print(data,type(data))

data=[[1,2],[2,3],[3,4]]
data=np.array(data)
print(data,type(data))
'''
'''
#indexing 1D
data=np.array([1,2,3,4,5,6,7,8,9])
print(data[0])
print(data[1])
print(data[-1])
print(data[-5])
'''
#indexing 2D[row index , column index]
'''
data=np.array([[1,2],[3,4],[5,6]])
print(data[0,0])
print(data[1,0])

data=np.arange(10,161,10)
data=data.reshape(4,4)
print(data)
x=data[:2,:2]
#x=data[:,:]
x=data[:2:-1,:2:-1]
print(x)
'''


import pandas as pd
import numpy as np

df=pd.read_csv("d:/Book1.csv")
#print(df)
a=np.array(df)
#print(a)

for i in range(len(a)):
    #a[i,2]=a[i,2]*2
    a[i][0]=str(a[i][0]).lower()
    #print("record number",i+1,"\n",a[i])
    #print("record number",i+1,"\n",a[i][0])
#print(a)
np.savetxt("d:/test.csv",a,fmt='%s,%f,%f,%f',delimiter=",")