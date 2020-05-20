#10. Write a Python program to change a given string to a new string where
#the first and last chars have been exchanged. 

data = input("enter string: ")

new = data[-1] + data[1:-1] + data[0]

print(new)