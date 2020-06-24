class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Cource:
    def __init__(self,name_of_cource,max_students):
        self.name_of_cource = name_of_cource
        self.max_students = max_students
        self.students = []
        
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for i in self.students:
            value += i.get_grade()
            
        return value / len(self.students)
    
s1 = Student("bhavesh",25,60)
s2 = Student("abhishek",25,70)
s3 = Student("sanyukta",24,80)

cource = Cource("DBDA",3)
cource.add_student(s1)
cource.add_student(s2)
cource.add_student(s3)
print(cource.students[0].name)
print("Average grade of all students-->",cource.get_average_grade())


