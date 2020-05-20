'''17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses '''

def insert_end(str1,n):
    a = ""
    for i in range(n):
        a = a + str1[-2:]
        
    return a

n = int(input("enter number: "))

str1 = input("enter syring: ")

print(insert_end(str1, n))
        
    



