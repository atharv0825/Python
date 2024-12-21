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

