try :
    num1,num2 = eval(input("Enter two numbers , separated by comma : "))
    result = num1/num2
    print("Result is ",result)


except ZeroDivisionError:
    print("Division by zero is error !!!!!")

except SyntaxError :
    print("Comma is missing . Enter the number separated by comma like this 1,2 ")

except:
    print("Wrong input ")

else :
    print("No exception")

finally:
    print("This print will execute no matter Whatttttt !!!!!!")