'''19. Write a Python program to get the last part of a string before a specified character. 
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python '''

data = "https://www.w3resource.com/python-exercises"

sdata = data.split("-")



print("".join(sdata[:-1]))



