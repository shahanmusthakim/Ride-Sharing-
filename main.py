from ride import Ride, Ridematching,RideRequest,RideSharing
from user import Driver,Rider
from vehicle import Bike,Car


from ride import RideSharing
from user import Driver, Rider

WannaGo = RideSharing("Wanna_Go")

rahim = Rider("Rahim", "rahim@gmail.com", 1234, "Zindabazar", 4000)

WannaGo.add_riders(rahim)

karim = Driver("Karim", "karim@gmail.com", 1435, "Bondor")

WannaGo.add_drives(karim)

print(WannaGo)

rahim.request_ride(WannaGo, "Patantula", 'car')

karim.reach_destination(rahim.current_ride)

rahim.show_current_ride()

print("\nRider Wallet:", rahim.wallet)
print("Driver Wallet:", karim.wallet)
