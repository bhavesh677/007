'''10. Write a Python program to find the list of words that are longer than n from
a given list of words'''

#method 1
'''
def find(data,x):
    words=[]
    for i in data:
        if len(i)>x:
            words.append(i)
    return words

mylist=['bhavesh','abhi','sanyu','yash']
n=int(input("which lenth of word you want?"))

print("Result--->",find(mylist,n))
'''

#method 2
'''
def finds(data,x):
    words = []
    s = data.split(" ")
    for i in s:
        if len(i) > x:
            words.append(i)
    return words

mydata="bhavesh abhi sanyu yash"
n=int(input("which lenth of word you want?"))

print(finds(mydata,n))
'''






