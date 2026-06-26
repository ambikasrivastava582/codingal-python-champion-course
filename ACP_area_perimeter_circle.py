import math

# Class Definition
class Circle:
    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate area
    def area(self):
        return math.pi * self.radius ** 2

    # Method to calculate perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# Main Program
r = float(input("Enter the radius of the circle: "))

# Create object
c = Circle(r)

# Display results
print(f"\nRadius: {c.radius}")
print(f"Area of Circle: {c.area():.2f}")
print(f"Perimeter (Circumference) of Circle: {c.perimeter():.2f}")