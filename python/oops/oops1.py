class Human():
    
    def give_name(self):
        self.name = input("Name: ")
        
    def give_gender(self,g="Unknown"):
        self.gender = g
        
    def give_education(self):
        self.edu = input("You are: ")
        
    def intro(self):
        print(self.name,self.gender,self.edu)
