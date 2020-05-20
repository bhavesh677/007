#12. Write a Python program to count the occurrences of each word in a given sentence

data = "Write a Python program to to count the occurrences of each word in a given sentence"

ndata = data.split()

occurance = dict()

for i in ndata:
    if i in occurance.keys():
        occurance[i] = occurance[i] + 1
        
    else:
        occurance[i] = 1
        
print(occurance)
        




