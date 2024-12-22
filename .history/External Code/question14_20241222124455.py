# Multilevel inheritance
class Grandfather:
        def __init__(self,g_age):
                self.age = g_age
        def details(self, age):
                print(f"I am Grandfather my age is {self.age}") 

class father(Grandfather):
        def __init__(self,age):
                super.__init__(age)