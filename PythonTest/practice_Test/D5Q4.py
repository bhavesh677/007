'''4.	Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]'''

List1 = ["M","na","i","bha"]
List2 = ["y","me","s","vesh"]

final = []

for i,j in zip(List1,List2):
    final.append((i+j))
    
print(final)
    





