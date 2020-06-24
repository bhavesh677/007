# Class attributes and class methods

class Person:
    number_of_peopel = 0  #this is class attribute
    
    def __init__(self,name):
        self.name = name
        #Person.number_of_peopel += 1 #to keep track of entries
        Person.add_person()
    
    @classmethod #decorator
    def number_of_entries(cls):
        return cls.number_of_peopel
    
    @classmethod
    def add_person(cls):
        cls.number_of_peopel += 1





#print(Person.number_of_peopel)       

print(Person.number_of_entries()) 

p1 = Person("Tim")

#print(Person.number_of_peopel)

print(Person.number_of_entries()) 

p2 = Person("Jill")

print(Person.number_of_peopel)



#Person.number_of_peopel = 8

print(p1.number_of_peopel)

#Person.number_of_peopel = 9 

print(p2.number_of_peopel)
