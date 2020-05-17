def findint(entry):
    
    
    istr=[int(i) for i in entry.split() if i.isdigit()]
    
    return istr

#str="English = 78 Science = 83 Math = 68 History = 65"

str=input("Enter string")

num=findint(str)

sm=sum(num)

cnt=len(num)

print("SUM: ",sm)


print("Average: ",sm/cnt)


    

