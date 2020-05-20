#9. Write a Python program to remove the nth index character from a nonempty string


data = "bhavesh"

n = int(input("enter index: "))

def IR(data,n):
    if (n < len(data) and data != ""):
        return (data[:n] + data[n+1:])
    else:
        return "invalid index enterd or data is empty"
    
print(IR(data,n))
        
