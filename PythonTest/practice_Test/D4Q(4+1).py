def showStudent(name, Id, college):
    print("Student ID: %s , Name: %s , College Name:  %s"%(Id,name,college))
    
name = input("Enter name: ")
Id = input("Enter ID: ")
college = input("Enter college name: ")

if name != "" and Id != "" and college != "":
    showStudent(name, Id, college)
    
elif name !="" and Id == "" and college != "":
    showStudent(name,Id="1",college=college)
    
elif name !="" and Id != "" and college == "":
    showStudent(name, Id, college="Vita")
    
else:
    showStudent(name, Id="1", college="Vita")