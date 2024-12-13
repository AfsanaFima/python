class  Employee:
    def __init__(self) :
        print("Employee object created")

    def __del__(self):
        print("Employee object deleted")


def create_employee():
    print("Creating employee object ")
    emp1 = Employee()
    return emp1

print("Creating employee creation function")
create_employee()
print("Programe end ")