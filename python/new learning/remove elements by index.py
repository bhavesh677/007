data = ["red","green","white","black","pink","yellow"]

'''rlist = [0,4,5]
j = 0
for i in rlist:
    
    data.pop(i - j)
    j += 1
    
print(data)'''


data = [v for i,v in enumerate(data) if i not in (0,4,5)]

print(data)