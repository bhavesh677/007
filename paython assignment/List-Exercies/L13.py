#13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 


import pprint


array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]


pprint.pprint(array)
