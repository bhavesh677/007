#20. Write a Python function to reverses a string if it's length is a multiple of 4. 

def multiple(str1):
    if len(str1) % 4 == 0:
        return str1[::-1]
    
print(multiple("bhaveshh"))

