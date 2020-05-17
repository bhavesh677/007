#5. How to assign name to the series’ index?
import pandas as pd
import numpy as np
s=pd.Series(['bhavesh','DBDA','007'])
s.index.name='number'
print(s)