# Multilevel inheritance
class Grandfather:
        def __init__(self,g_age):
                self.g_age = g_age
        def details(self, g_age):
                print(f"I'm Grandfather my age is {self.g_age}") 

class father(Grandfather):
        def __init__(self,g_age,f_age):
                super.__init__(g_age)
                self.f_age = f_age
        def details(self):
                super().details()
                print(f"\n I'm Father my age is {self.f_age}")

class child(father):
        def __init__(self, g_age, f_age, c_age):
                super().__init__(g_age, f_age)
                self.c_age = c_age
        def details(self):
                super().details()
                print(f"\n I'm child my age is {self.c_age}")        

child1 = child(78,40,15)
child                