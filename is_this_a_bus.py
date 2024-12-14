class vehicle :
    def __init__(self,name,max_speed,mileage) :
        self.name = name
        self.max_speed = max_speed
        self.mileage  = mileage

class Bus (vehicle) :
    pass

class Car(vehicle):
    pass

v1 = vehicle("fer",130,18)
school_bus = Bus("school volvo",180,12)
car = Car ("Audi Qs",250,20)


print("_____VEHICLE DETAILS_____")
print("Name : {} ,Max speed : {} ,Mileage : {}".format(school_bus.name,school_bus.max_speed,school_bus.mileage))
print("Name : {} ,Max speed : {} ,Mileage : {}".format(car.name,car.max_speed,car.mileage))
        