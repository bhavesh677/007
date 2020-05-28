class dog:
    
    def __init__(self,name):
        self.name1 = name
        print(name)
    
    def add_one(self,x):
        return x + 1
    
    def bark(self):
        print("Bark")
'''        
d = dog()

d.bark()

print(d.add_one(6))

'''

d = dog("Tommy")

d2 = dog("Bill")

