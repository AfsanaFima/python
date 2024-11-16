weather = (0,1,1,1,0,0,1)
sunny = 0
rainy = 0

for i in range (0,7) :
    if weather[i] == 1 :
        sunny = sunny + 1

    else:
        rainy = rainy + 1


if(sunny>rainy) :
    print("It's going to be a sunny week ")

else:
    print("It's going to be a rainy week ")