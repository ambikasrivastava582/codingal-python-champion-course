# Operator Overloading Example

class Number:
    def __init__(self, value):
        self.value = value

    # Overloading + operator
    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print("Value:", self.value)


# Main Program
num1 = Number(20)
num2 = Number(30)

result = num1 + num2

print("First Number:", num1.value)
print("Second Number:", num2.value)
result.display()