'''4. Write a Python program to get a string from a given string where all occurrences of its
 first char have been changed to '$', except the first char itself. '''
 
data = 'restart'
 
a = data[0]

data = data.replace(a, "$")

new = a + data[1:]

print(new)

        



