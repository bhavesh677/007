'''
l=[]
for i in range(1,11):
    l.append(i)

print(l)

#List comprihension
l=[i for i in range(1,11)]
print(l)
'''
'''
l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
l3=[]

for i in range(len(l1)):
    l3.append(l1[i]*l2[i])
    
print(l3)

#list comprihension

l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
#l3=[i*j for i in l1 for j in l2]
l3=[l1[i]*l2[i] for i in range(len(l1))]
print(l3)
'''
'''
l1=['bhavesh','abhishek','sanyukta']
l2=['precat','dbda','fish']

l3=[i+"---"+j for i in l1 for j in l2]
print(l3)
'''
'''
#scalar multiplication

l=[1,2,3,4,5]
l1=[i*2 for i in l]
print(l1)
'''

#conditional data entry

l=[1,2,3,4,5,6,7,8,9,10]
l1=[i for i in l if i%2==0]
print(l1)

l=[i for i in range(1,1001) if i%3==0 and i%7==0 ]
print(l)






