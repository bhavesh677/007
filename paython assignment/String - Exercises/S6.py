'''6. Write a Python program to add 'ing' at the end of a given string 
(length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged. 
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly' '''

def ing(str):
    if (len(str) >= 3):
        if (str[-3:] == "ing" or str[-3:] == "ING"):
            return str + "ly"
        else:
            return str + "ing"
    else:
        return "lenth is less than 3"
    
data=input("Enter word: ")

print(ing(data))








        



