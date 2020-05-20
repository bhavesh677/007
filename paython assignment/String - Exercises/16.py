'''16. Write a Python function to insert a string in the middle of a string. 
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''

def insert_string_middle(str1,str2):
    l = len(str1)
    print(l)
    if l % 2 == 0:
        return str1[:l//2] + str2 + str1[l//2:]
    
print(insert_string_middle("{{}}", "PHP"))


