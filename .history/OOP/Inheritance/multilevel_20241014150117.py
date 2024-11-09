class Vehicle:
    def __init__(self,wheels,fuel_type,speed):
        self.wheels = wheels
        self.fuel_type = fuel_type
        self.speed = speed

    def display_vehicle_info_(self):
        print(f"Vehicle info : Wheels : {self.wheels} , fuel type : {self.fuel_type} , speed : {self.speed} \n")

class car(Vehicle):
    def __init__(self, wheels, fuel_type, speed,doors,transmission,engine_type):
        super().__init__(wheels, fuel_type, speed)
        self.doors = doors
        self.transmission = transmission
        self.engine_type = engine_type

    def display_car_info_(self):
        super().display_vehicle_info_()    
        print(f"Car")

class ElectricCar(car):
    def __init__(self, wheels, fuel_type, speed , doors , transmission , engine_type , battery_capacity , charging_type):
        super().__init__(wheels, fuel_type, speed)