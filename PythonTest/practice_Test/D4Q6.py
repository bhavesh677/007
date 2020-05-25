'''6.Write a program to obtain the sum of the first and last digit of this number
2 user defined functions
1st for first digit
2nd for last digit
Example:
 Input:  5424
Output: 9
'''

def FirstDigi(n):
    return n[0]

def LastDigi(n):
    return n[-1]

n = input("Enter a number: ")

F = int(FirstDigi(n))
L = int(LastDigi(n))

print("Sum of first and last digit of %s is--> %d"%(n,(F+L)))

