# Multilevel inheritance
class Grandfather:
        def __init__(self,age):
                self.age = age
        def details(self, age):
                print(f"I am Grandfather my age is {self.age}") 

class father(Grandfather):
        def __init__()