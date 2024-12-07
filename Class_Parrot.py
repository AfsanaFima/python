class Parrot :
    species = "bird"

    def __init__(self,name ,age) :
        self.name = name 
        self.age = age

p1 = Parrot ("Polly",18)
p2 = Parrot ("kisha",34)

print("Polly is a  ",p1.species)
print("Kisha is a  ",p2.species)

print("{} is {} is years old ".format(p1.name,p1.age))
print("{} is {} is years old ".format(p2.name,p2.age))
