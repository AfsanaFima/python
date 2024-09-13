import turtle
sp=turtle.Screen()
sp.bgcolor("light pink")
t = turtle.Turtle()
sp.title ("Turtleeeeee")
size = 0

while True :
    for i in range (4) :
        t.fd(size+1)
        t.left(90)
        size = size - 5
    size = size +1