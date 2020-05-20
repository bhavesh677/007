''' 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from
 a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with
 'good'. Return the resulting string. '''
 
data = 'The lyrics is poor!'

s = data.find("not")
e = data.find("poor")

if s < e and s >= 0 and e >= 0 : 
    ndata = data.replace(data[s:(e+4)],"good")

    print(ndata)
    
else:
    print(data)
    