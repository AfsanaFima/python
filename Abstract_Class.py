from abc import ABC ,abstractmethod

class ABclass(ABC):
    def print (self, x):
        print("Passed value is:",x)

    @abstractmethod
    def task(self):
        print("we're inside of the ABclass method")

class testClass (ABclass):
    def task(self):
        print("We're inside of the testclass method")


t1 = testClass()
t1.task()
t1.print(7)