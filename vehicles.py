# Base class (optional)
class Vehicle:
    def move(self):
        pass  # Base method, will be overridden
class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing ⛵")
my_car = Car()
my_plane = Plane()
my_boat = Boat()
my_car.move()    # Output: Car is driving 🚗
my_plane.move()  # Output: Plane is flying ✈️
my_boat.move()   # Output: Boat is sailing ⛵
vehicles = [my_car, my_plane, my_boat]

for vehicle in vehicles:
    vehicle.move()  # Calls the correct move() for each object
