# single inheritance
class person:
   def __init__(self , name , age):
      self.name = name
      self.age = age

   def display_details(self):
      print(f"Name : {self.name}")
      print(f"Age : {self.age}")
