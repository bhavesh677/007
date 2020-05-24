#2.From a list containing ints, strings and floats, make three lists to store them separately.

def Sep(mixlst):
    
    for i in mixlst:
        
        Ilst = [i for i in mixlst if isinstance(i,int)]
        
        Flst = [i for i in mixlst if isinstance(i,float)]
        
        Slst = [i for i in mixlst if isinstance(i, str)]
        
    return Ilst,Flst,Slst

mixlist = [0,"bhavesh",0,"sawant",9.4,7,"vita",7.4,"dbda"]

Int,Float,String = Sep(mixlist)

print(Int)
print(Float)
print(String)

        
