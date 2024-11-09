
class car :
        def __init__(self,company,model,year,distance):
                self.company = company
                self.model = model
                self.year = year

        def carInfo(self):
                return f"{self.company} {self.model} {self.year}"

        def status(self)        