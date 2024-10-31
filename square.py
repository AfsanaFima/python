import turtle
import random


window = turtle.Screen()
window.bgcolor("lightblue")  
window.setup(width=1.0, height=1.0)  
square_turtle = turtle.Turtle()
square_turtle.speed(0)  


colors = ["red", "blue", "yellow", "green", "purple", "orange", "white"]

#
def draw_squares():
    side_length = 50  
    while True:
        square_turtle.color(random.choice(colors))  
        for _ in range(4):
            square_turtle.forward(side_length)
            square_turtle.right(90)
        square_turtle.right(10)  
        side_length += 2


draw_squares()


turtle.done()
