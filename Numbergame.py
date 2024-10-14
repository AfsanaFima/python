import random 
playing = True
num = str(random.randint(10,100))


print("I will genarate a number from 10 to 100 , you are going to guess the number and digit at a time .")

while True:
    guess = (input("Give me your best guess mate!!! \n"))
    if num ==guess:
       print("You win the gameee")
       print("The number was ",num)
       break
    else:
        print("Your guess isn't correct (-_-) try again mate \n")
