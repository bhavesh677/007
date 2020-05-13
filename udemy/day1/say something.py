def change(x):
    interogatives=("why","what","who","where","when")
    a=x.capitalize()
    if x.startswith(interogatives):
        return "{}?".format(a)
    else:
        return "{}".format(a)
lst=[]    
    
while True:
    f=input("say something: ")
    if f == "\end" :
        break
    else:
        lst.append(change(f))

print(" ".join(lst))    
