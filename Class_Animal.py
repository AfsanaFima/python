from abc import ABC ,abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Dog(animal):
    def move(self):
        print("Dog hass four legs")

class Snake(animal):
    def move(self):
        print("Snake does'nt have legs")

class human(animal):
    def move(self):
        print("Human has two legs")


class panda(animal):
    def move(self):
        print("Panda is round and cute .")

class bird(animal):
    def move(self):
        print("Birds can fly <3")



a1 = Dog()
a1.move()




