
from datetime import datetime
from vehicle import Car, Bike


class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.drivers = []
        self.riders = []
        self.rides = []

    def add_riders(self, rider):
        self.riders.append(rider)

    def add_drives(self, driver):
        self.drivers.append(driver)

    def __str__(self):
        return f'Company Name: {self.company_name} with riders: {len(self.riders)} and Drivers: {len(self.drivers)}'


class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.vehicle_type = vehicle
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)

    def set_driver(self, driver):
        self.driver = driver

    def set_rider(self, rider):
        self.rider = rider

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.driver.wallet += self.estimated_fare
        self.rider.wallet -= self.estimated_fare

    def calculate_fare(self, vehicle_type):
        distance = 10

        fare_per_km = {
            'Car': 40,
            'Bike': 30,
            'CNG': 25
        }

        if vehicle_type not in fare_per_km:
            raise ValueError("Invalid vehicle type")

        return distance * fare_per_km[vehicle_type]

    def __repr__(self):
        return f'Ride from {self.start_location} to {self.end_location}'


class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class Ridematching:
    def __init__(self, driver):
        self.available_drivers = driver

    def find_driver(self, ride_request, vehicle_type):

        if len(self.available_drivers) == 0:
            print("No driver available")
            return None

        print("Looking for Driver.......\n")

        driver = self.available_drivers[0]

        if vehicle_type == 'car':
            vehicle = Car("Car", "ACD124", 50)

        elif vehicle_type == 'bike':
            vehicle = Bike("Bike", "BKG64", 40)

        else:
            raise ValueError("Invalid vehicle type")

        ride = Ride(
            ride_request.rider.current_location,
            ride_request.end_location,
            vehicle
        )

        driver.accept_ride(ride)

        return ride
