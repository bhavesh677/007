'''3. Write a Python program to get a string made of the first 2 and the last 2 chars 
from a given a string. If the string length is less than 2, return instead of the empty string.''' 


data ='w'

def FL(data):
    if len(data) < 2:
        return ""
    else:
        return (data[:2]+data[-2:])
    
print(FL(data))