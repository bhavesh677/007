'''5. Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''

st1 = "abc"
st2 = "xyz"

nst1 = st2[:2] + st1[2:]
nst2 = st1[:2] + st2[2:]

print(" ".join([nst1,nst2]))
