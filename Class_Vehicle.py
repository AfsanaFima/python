class vehical :
    def __init__(self ,model,max_speed,mileage):
        self.model = model
        self.max_speed = max_speed
        self.mileage   = mileage

c1 = vehical ("Toyota",180,12)
c2 = vehical("BMW",110,10)
c3 = vehical("Audi",200,15)


print("C 1--->","Model : ",c1.model,"Max speed : " ,c1.max_speed,"Mileage : ",c1.mileage)
print("C 2--->","Model : ",c2.model,"Max speed : " ,c2.max_speed,"Mileage : ",c2.mileage)
print("C 3--->","Model : ",c3.model,"Max speed : " ,c3.max_speed,"Mileage : ",c3.mileage)