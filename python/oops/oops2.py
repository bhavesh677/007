class dog:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #print(name)
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age
    
    def bark(self):
        print("Bark")
    
'''        
d = dog()

d.bark()

print(d.add_one(6))

'''

d = dog("Tommy",7)
print(d.get_name())
d.set_age(8)
print(d.get_age())

d2 = dog("Bill",4)
print(d2.get_name())
d2.set_age(5)
print(d2.get_age())
