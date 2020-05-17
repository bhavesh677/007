#find the leap years in given year range
import pandas as pd
import numpy as np
a=int(input("enter starting year:"))
b=int(input("enter ending year:"))
years=np.arange(a,b+1)
l=list(years)
l1=[i for i in l if i%4==0 or (i%400==0 and i/100!=0)]
print("leap years in the given range are:",l1,"\n","count is:",len(l1))

