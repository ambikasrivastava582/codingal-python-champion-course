# Parent Class
class Bus:
    def __init__(self, distance):
        self.distance = distance
        self.rate = 10  # Fare per kilometer

    def calculate_fare(self):
        return self.distance * self.rate


# Child Class
class Passenger(Bus):
    def __init__(self, name, age, distance):
        super().__init__(distance)
        self.name = name
        self.age = age

    def final_fare(self):
        fare = self.calculate_fare()

        # 50% discount for senior citizens
        if self.age >= 60:
            fare = fare * 0.5

        return fare

    def display(self):
        print("\n----- Bus Fare Details -----")
        print("Passenger Name :", self.name)
        print("Age            :", self.age)
        print("Distance       :", self.distance, "km")
        print("Total Fare     : ₹", self.final_fare())


# Main Program
name = input("Enter passenger name: ")
age = int(input("Enter age: "))
distance = float(input("Enter distance (km): "))

p = Passenger(name, age, distance)
p.display()