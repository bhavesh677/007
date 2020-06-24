# Static methods

class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("Run")
        
print(Math.add5(3)) # we dont need to create instance to use these methods

print(Math.add10(10))

Math.pr()

