#3. How to convert the index of a series into a column of a dataframe?
import pandas as pd
import numpy as np

s=pd.Series(['bhavesh','007','VITA','DBDA'],name="myself")
print(s,type(s))

dfr=s.to_frame()
dfr.reset_index(level=0, inplace=True)

print( dfr.to_string(index=False))
#dfr['number'] = dfr.index 
#print(dfr.to_string(index=False))
