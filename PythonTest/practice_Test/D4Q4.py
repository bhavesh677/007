'''4.Create a function showStudent() in such a way that it should accept 
student id, name, and it’s college name  and if the id and college name is missing in function 
call it should show it as by default id is 1 and college name  is VITA.'''

def showStudent(name, Id="1", college="vita"):
    print("Student ID: %s , Name: %s , College Name:  %s"%(Id,name,college))


name = input("Enter name: ")
Id = input("Enter ID: ")
college = input("Enter college name: ")

if Id != "" and college != "":
    showStudent(name,Id,college)
    
else:
    showStudent(name)


