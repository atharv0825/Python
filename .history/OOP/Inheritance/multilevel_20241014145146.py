class Vehicle:
    def __init__(self,wheels,fuel_type,speed):
        self.wheels = wheels
        self.fuel_type = fuel_type
        self.speed = speed

    def display_vehicle_info_(self):
        print(f"Vehicle info : Wheels : {self.wheels} , fuel type : {self.fuel_type} , speed : {self.speed}")


class ElectricCar(Vehicle):
    def __init__(self, wheels, fuel_type, speed , doors , transmission ):
        super().__init__(wheels, fuel_type, speed)