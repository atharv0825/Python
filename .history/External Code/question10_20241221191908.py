# 10. program for class, object and constructor using suitable data

class student :
    def __init__(self,rollNo,name,age):
        self.rollNo =rollNo
        self.name = name
        self.age = age 
    
    def display_details(self):
        print(f"Name : {self.name} Roll No : {self.rollNo} age : {self.age}") 


student1 = student(10,"Atharv",21)
student2 = student(12,"Shatkon",)                      