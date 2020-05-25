'''3.	Write a recursive function to calculate the sum of numbers from 0 to 10
Expected output: 55'''

def SUM(n):
    if n < 1:
        return n
    else:
        return n + SUM(n-1)

print(SUM(2956))
    
        

