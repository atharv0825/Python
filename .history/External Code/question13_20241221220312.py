# single inheritance
class person:
   def __init__(self , name , age):
      self.name = name
      self.age = age

   def display_details(self):
      print(f"Name : {self.name}")
      print(f"Age : {self.age}")


class student(person):
   def __init__self(self,name,age,student_id):
    self.__init__(name , age)    
    self.student_id = student_id

   def display_details(self):
      self.display_details()
      print(f"Student Id : {self.student_id}")

student1 = student1("Atharv" , 21 , "A237")
student1.display_details()