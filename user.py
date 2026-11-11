
from abc import ABC, abstractmethod
from ride import RideRequest, Ridematching


class Users(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        pass


class Rider(Users):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_ride = None
        self.current_location = current_location
        self.wallet = initial_amount

    def display_profile(self):
        print(f'Name: {self.name}\tEmail: {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print('Amount must be positive')

    def update_location(self, new_location):
        self.current_location = new_location

    def request_ride(self, ride_sharing, destination, vehicle_type):

        ride_request = RideRequest(self, destination)

        ride_matching = Ridematching(ride_sharing.drivers)

        ride = ride_matching.find_driver(ride_request, vehicle_type)

        if ride is None:
            return

        self.current_ride = ride
        ride.set_rider(self)

        ride_sharing.rides.append(ride)

        print('WE GOT A RIDE :)')

    def show_current_ride(self):

        if self.current_ride is None:
            print("No current ride")
            return

        print('\n------- RIDE DETAILS -------\n')
        print(f'Rider: {self.name}')
        print(f'Driver: {self.current_ride.driver.name}')
        print(f'Selected Vehicle: {self.current_ride.vehicle_type.vehicle_type}')
        print(f'Started Location: {self.current_ride.start_location}')
        print(f'End Location: {self.current_ride.end_location}')
        print(f'Total Cost: {self.current_ride.estimated_fare}')


class Driver(Users):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location

    def display_profile(self):
        print(f'Name: {self.name}')

    def accept_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self)

    def reach_destination(self, ride):
        ride.end_ride()
        print("Ride completed!")
