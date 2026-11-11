from abc import ABC
class Vehicle(ABC):
    speed = {
        'car': 200,
        'bike': 120
    }

    def __init__(self, vehicle_type, licence_plate, rate):
        self.vehicle_type = vehicle_type
        self.licence_plate = licence_plate
        self.rate = rate


class Bike(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate):
        super().__init__(vehicle_type, licence_plate, rate)


class Car(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate):
        super().__init__(vehicle_type, licence_plate, rate)
