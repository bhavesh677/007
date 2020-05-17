'''5. Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''




def my_cnt(data):
    cnt=0
    for i in data:
        if len(i)>1 and i[0] == i[-1]:
            cnt+=1
    return cnt

slist=['abc', 'xyz', 'aba', '1221']
print(my_cnt(slist))