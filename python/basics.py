'''def mean(data):
    if type(data) == dict:
        my_mean= sum(data.values()) / len(data)
    
    else:
        my_mean=sum(data)/len(data)
        
    return my_mean

temp=[3,5,6,7,6,9]
grades={"sam" : 4,"dam" : 6}

print(mean(temp))
print(mean(grades))'''

x=1.4


#print(isinstance(x, int))

#string formating
'''
name=input("enter your name: ")
message="hello %s!" % name
#message=f"Hello {name}!"
print(message)
'''
'''
name=input("enter name: ")
surname=input("enter surname: ")
when="today"
message= "hello %s %s what's up %s" % (name,surname,when)
#message=f"hello {name} {surname} what's up {when}"
print(message)
'''
'''
a="bhavesh"
print(a.title())
'''
a,b=3,2
print(a,b)
b,a=a,b
print(a,b)