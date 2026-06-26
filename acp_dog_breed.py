class Dog:
    
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Dog class
labrador = Dog("lab", 10)
pamalion = Dog("pam", 15)

# access the class attributes
print("lab is a {}".format(labrador.species))
print("pam is also a {}".format(pamalion.species))

# access the instance attributes
print("{} is {} years old".format(labrador.name, labrador.age))
print("{} is {} years old".format(pamalion.name, pamalion.age))