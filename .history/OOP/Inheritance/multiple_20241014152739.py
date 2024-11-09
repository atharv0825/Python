class Vehicle:
    def __init__(self,wheels,fuel_type) :
        self.wheels = wheels
        self.fuel_type = fuel_type

    def display_vehicle_info_(self):
        print(f"Vehicle info \n  wheels : {self.wheels} , fuel type : {self.fuel_type}")

class electric_car:
    def __init__(self,battery_capacity,charging_time):
        self.battery_capacity = battery_capacity
        self.charging_time = charging_time

    def display_ElectricCar_info_(self):
             
