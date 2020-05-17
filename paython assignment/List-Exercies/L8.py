#8. Write a Python program to check a list is empty or not. 

#method 1
'''mylist=[5]
l=[]

if mylist == l:
    print("list is empty")
else :
    print("list is not empty")'''
    
    
#method2
'''def Enquiry(lis1): 
    if len(lis1) == 0: 
        return 0
    else: 
        return 1
          
# Driver Code 
lis1 = [6] 
if Enquiry(lis1): 
    print ("The list is not empty") 
else: 
    print("Empty List") 
'''


#method ***most preferable***  

def Enquiry(lis1): 
    if not lis1: 
        return 1
    else: 
        return 0
          
# Driver Code 
lis1 = [] 
if Enquiry(lis1): 
    print ("The list is Empty") 
else: 
    print ("The list is not empty")
