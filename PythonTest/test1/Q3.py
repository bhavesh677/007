mixstr=input("Enter string: ")

def UL(mixstr):
    n1=""
    n2=""
    for i in mixstr:
        if i.islower():
            n1=n1 + i
            
        else:
            n2=n2 + i
            
    return n1 + n2


print(UL(mixstr))