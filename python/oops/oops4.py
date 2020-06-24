# Inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("I don't know how to speak")
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    
    def speak(self):
        print("meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old I am {self.color}")
        
        
class Dog(Pet):
    def speak(self):
        print("bark")

class Fish(Pet):
    pass

p = Pet("tommy",4)

p.show()

c = Cat("pinky",2,"white")
c.show()
c.speak()

d = Dog("jim",6)
d.show()
d.speak()

f = Fish("bubbles",1)
f.show()
f.speak() 
        


