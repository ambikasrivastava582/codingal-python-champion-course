# Parent Class
class Vehicle:
    def move(self):
        print("Vehicle is moving.")


# Child Class 1
class Car(Vehicle):
    def move(self):
        print("Car is driving on the road.")


# Child Class 2
class Bike(Vehicle):
    def move(self):
        print("Bike is riding on the road.")


# Child Class 3
class Bus(Vehicle):
    def move(self):
        print("Bus is carrying passengers.")


# Child Class 4
class Airplane(Vehicle):
    def move(self):
        print("Airplane is flying in the sky.")


# Main Program
vehicles = [Car(), Bike(), Bus(), Airplane()]

print("Vehicle Movements:\n")

for vehicle in vehicles:
    vehicle.move()