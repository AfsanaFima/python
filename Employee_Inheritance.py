class person :
    def __init__(self,name,age) :
        self.name = name
        self.age = age 

    def display(self) :
        print("Name : {},Age : {} ,".format(self.name,self.age))

class employee (person) :
    def __init__(self, name, age,employee_id,salary):
        self.employee_id = employee_id
        self.salary = salary
        super().__init__(name, age)

    def display2(self) :
        super().display()
        print("Employee ID : {} ,Salary : {}".format(self.employee_id,self.salary))

em = employee ("Albert",35,3335,98765)
em.display2()

print(issubclass(employee,person))