import random
import time

num = random.randint(1,100)

def intro():
    print("Welcome to the number Guesssing game !!!")
    global name 
    name = input("What's your name ?")
    print(name +"We will play a game.I am thinking of a number between 1 and 100.")
    if(num% 2 == 0):
        x = "even"
    else:
        x = "odd"
        print("The is an " + x + "number")
        time.sleep(0.5)
        print("You have 5 chances to guess the number .")

def pick ():
    guessTaken = 0

    while guessTaken < 6 :
        time.sleep(0.25)
        guess = int(input("Take a guess : "))

        try:
            if guess <= 100 and guess >= 1 :
                guessTaken +=1
                if guessTaken <6:
                    if guess < num :
                        print("Your guess is too low")
                    if guess >num :
                        print("Your guess is too high")
                    if guess != num :
                        time.sleep(0.25)
                        print("Try again -_- !!")
                    if guess == num :
                        break
            if guess > 100 and guess < 1  :
                print("your guess is out of range .Try again.")
                time.sleep(0.25)      
                print("Pleas enter a number between 1 and 100 .")

        except:
            print("Please enter a valid number .")
        
    if guess == num :
        guessTaken  = str (guessTaken)
        print("Excellent workk!!! {}!! You have guessed the number in {} guesses!".format(name,guessTaken))
    
    if guess!= num :
        print("Sorry .Iwas thinking of another number : " + str(num))

playagain = "yes"
while playagain == 'yes' or playagain == 'y' or playagain == 'Yes' :
    intro()
    pick()
    print("Do you want to play again ?!! <3 (Yes or NO) (y/n)")
    playagain = input()