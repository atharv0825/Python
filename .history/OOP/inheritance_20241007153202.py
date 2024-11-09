
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def getinfo(self):
        return f"Name : {self.name} Age : {self.age} Salary : {self.salary}"

class Manager:
    def __init__(self,name, age, salary,department):
        super().__init__(name,age , salary)
        self.d           