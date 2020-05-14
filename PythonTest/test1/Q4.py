entry=input("Enter string: ")

def Findint(entry):
    lst=[]
    
    for i in entry:
        if i.isdigit():
            lst.append(i)
            
        else:
            continue
    
    return lst

a=Findint(entry)
b=[]
for i in range(len(a)):
    b[i]=int(a[i])
    
print(b)
    

