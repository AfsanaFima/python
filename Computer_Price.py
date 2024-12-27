class Computer :
    def __init__(self):
        self.__maxprice = 5000


    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price

v1 = Computer()
v1.sell()

v1.__maxprice = 10000
v1.sell()

v1.setMaxPrice(10000)
v1.sell()