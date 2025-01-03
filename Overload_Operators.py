class A :
    def __init__(self,a):
        self.a = a


    def __lt__(self,other):
        if(self.a < other.a) :
            return "Object 1 is less than object 2"
        
        else:
            return "Object 2 is less than object 1"
        
    def __eq__(self, other):
        if(self.a == other.a) :
             return "Both objects are equal"
        
        else:
            return "Not equal"
       

ob1 =A (4)
ob2 = A (6)

print("Passed value  : " , ob1.a,ob2.a)
print(ob1 < ob2)

ob3 = A(7)
ob4 = A (7)

print("Passed value  : " , ob3.a,ob4.a)
print(ob3 == ob4)

