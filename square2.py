import turtle


window = turtle.Screen()
window.bgcolor("lightblue")  # Change this to your desired background color
window.setup(width=1.0, height=1.0)  # Make sure the window fills the whole screen
square_turtle = turtle.Turtle()


def draw_squares():
    while True:
        for _ in range(4):
            square_turtle.forward(100)
            square_turtle.right(90)
        square_turtle.right(10)  
draw_squares()


turtle.done()
