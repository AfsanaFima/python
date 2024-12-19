class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

    def display_details(self):
        return f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}"

# Creating instances of Dog
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Daisy", "Poodle")

# Displaying details of each dog
print(dog1.display_details())
print(dog2.display_details())
