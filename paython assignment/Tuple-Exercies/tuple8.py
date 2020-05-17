#8. Write a Python program to create the colon of a tuple.
from copy import deepcopy
tup=('bhavesh','007',[],'vita')
print(tup)
tupcopy=deepcopy(tup)
tupcopy[2].append('DBDA')
print(tupcopy)
print(tup)