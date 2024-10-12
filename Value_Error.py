try :
    num = int(input("Enter a number : "))
    print ("The enteref number is : ")

except ValueError as ex :
    print("Exception : ", ex)