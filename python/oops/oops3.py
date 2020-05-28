'''1.Write python program to perform bank operations using class and objects.
       Conditions:
a.	Bank name should be static.
b.	Using menu driven program.
1 .Deposit
2. Withdraw
3. Exit
'''
class Bank:
    
    def __init__(self,balance):
        print("Wellcome to National Bank")
        self.balance = balance
        
    def Deposite(self):
        print("Your Balance is-->",self.balance)
        
        self.deposite = int(input("Pleas Enter Amount To Be Deposite: "))
        
        self.balance += self.deposite
        
        if self.deposite > 0:   
            print("You have succesfully Deposited-->",self.deposite)
            print("Your balance is-->",self.balance)
            
        else:
            print("Invalid Input Please Try Again!!!")
        
    def Withdraw(self):
        print("Your balance is-->",self.balance)
        
        self.withdraw = int(input("Please Enter Withdraw Amount: "))
        
        self.balance -= self.withdraw
        
        if self.withdraw > 0:
            print("Succesfully Withdrawn-->",self.withdraw)
            print("Balance is-->",self.balance)
            
        else:
            print("Invalid Input Please Try Again!!!")
            
    def Exit(self):
        self.exit = input("Press Q to Exit: ")
        if self.exit == "Q" or self.exit == "q":
            print("Exit Succesfull!!!")
        

customer_info = {1 : 5000, 2 : 7000 , 3 : 2000}

Acc_number = int(input("Enter Acc Number: "))
        
a = int(input("Press 1 to Deposite \nPress 2 to Withdraw\nPress 3 to Exit\n---> "))

objB = Bank(customer_info[Acc_number])

if a == 1:
    objB.Deposite()

elif a == 2:
    objB.Withdraw()

elif a == 3:
    objB.Exit()
        
            
            
            
            
        
        
        

        
        

