#Addition of two matrices

import numpy as np

lst1 = []
lst2 = []



print("Enter values in first 3*3 Matrix: ")
for i in range(9):
    lst1.append(int(input()))
    
print("Enter values in second 3*3 Matrix: ")
for i in range(9):
    lst2.append(int(input()))


    
Mat1 = np.asarray(lst1)
Mat2 = np.asarray(lst2)
    
Mat1 = Mat1.reshape(3,3)
Mat2 = Mat2.reshape(3,3)

Add = Mat1 + Mat2

print("Addition of Mat1 and Mat2 is:","\n",Add)


      




