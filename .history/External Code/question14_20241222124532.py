# Multilevel inheritance
class Grandfather:
        def __init__(self,g_age):
                self.g_age = g_age
        def details(self, g_age):
                print(f"I am Grandfather my age is {self.g_age}") 

class father(Grandfather):
        def __init__(self,g_age,f_age):
                super.__init__(age)