import numpy as np

data = np.arange(2000,3201)

def find(data):
    
      
    return [i for i in data if i%7 == 0 and i%5 != 0]
    

print((find(data)))
            

