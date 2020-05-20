'''14. Write a Python program that accepts a comma separated sequence of words as input 
and prints the unique words in sorted form (alphanumerically). '''

data = ["red", "white", "black", "red", "green", "black"]

udata = set(data)

sdata = sorted(udata)

print(sdata)


