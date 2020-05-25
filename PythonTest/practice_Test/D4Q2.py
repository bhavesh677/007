#2.Write a Python program to detect the number of local variables declared in a function.

def CLV():
    a = 2
    b = 4.6
    c = True
    d = False
    e = "bhavesh"
    f = [1,2,3,4]
    g = (0,7,0)
    h = {1,2,3,4,5}
    i = {"a":"A","b":"B"}
    j = 5
    print(len(locals()))
    
#print(CLV.__code__.co_nlocals)
    
CLV()


