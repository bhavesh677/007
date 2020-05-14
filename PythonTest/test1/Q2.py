str1=input("Enter main string: ")
str2=input("Enter middle string: ")


def Mstring(str1,str2):
    a=str1[0:len(str1)//2]

    b=str1[len(str1)//2:]

    new1="%s%s%s"%(a,str2,b)
    
    return new1

print(Mstring(str1,str2))


