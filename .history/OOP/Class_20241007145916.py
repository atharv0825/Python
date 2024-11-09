
class car :
        def __init__(self,company,model,year,distance):
                self.company = company
                self.model = model
                self.year = year
                self.distance = distance

        def carInfo(self):
                return f"{self.company} {self.model} {self.year}"

        def status(self):
                return f"{self.model} is currently in running condition"

        def traveled(self):
                return f""       