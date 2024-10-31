try:
    age = int(input("Enter your age: "))
    if 0 <= age <= 20:
        if age % 2 == 0:
            print("Valid age. It's even.")
        else:
            print("Valid age. It's odd.")
    else:
        print("Invalid age range.")
except ValueError:
    print("Invalid input.")
