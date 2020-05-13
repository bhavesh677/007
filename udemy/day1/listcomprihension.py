temps=[232,347,296,165]

'''t=[]

for i in temps:
    t.append(i/10)
    
print(t)'''

'''
r=[i/10 for i in temps]

print(r)
'''

'''
temps=[232,347,296,-987,165]

lst=[i/10 for i in temps if i != -987]
#lst=[i/10 for i in temps if i > 0]

print(lst)
'''

def foo(x):
    return sum([float(i) for i in x])


lst=['4.6','6.7']

print(foo(lst))


