def EO(n):
    if n >= 0:
        if n % 2 == 0:
            return "Entered number is Even"
        else:
            return "Entered number is Odd"
    else:
        return "invalid input"
        
n = int(input("Enter number: "))

print(EO(n))
        
        

