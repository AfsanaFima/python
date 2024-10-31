import turtle
import random

# Set up the turtle
window = turtle.Screen()
window.bgcolor("lightblue")  # Set background color
window.setup(width=1.0, height=1.0)  # Make sure the window fills the whole screen
square_turtle = turtle.Turtle()
square_turtle.speed(0)  # Set the turtle speed to maximum

# List of colors to choose from
colors = ["red", "blue", "yellow", "green", "purple", "orange", "white"]

# Draw squares indefinitely with varying colors and sizes
def draw_squares():
    side_length = 50  # Initial side length
    while True:
        square_turtle.color(random.choice(colors))  # Choose a random color
        for _ in range(4):
            square_turtle.forward(side_length)
            square_turtle.right(90)
        square_turtle.right(10)  # Slight rotation to create a pattern
        side_length += 2  # Increase the side length for the next square

# Start drawing
draw_squares()

# Finish drawing
turtle.done()
