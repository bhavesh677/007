'''5.Write a Python program to check whether a given number is a narcissistic number or not
For example, 371 is a narcissistic number; it has three digits, 
and if we cube each digits  3^3 + 7^3 + 1^3 the sum is 371. '''

'''test case = 371,153,370,407,1634,8208,9474 '''


def Narci(n,power):
    temp = n
    sum = 0
    while n != 0:
        r = n % 10
        sum += r**power
        n //= 10
    
    if sum == temp:
        return "Narcissistic Number"
    else:
        return "NOT Narcissistic Number"
    

n = int(input("Enter number: "))
power = len(str(n))
print(Narci(n,power))
        
        

