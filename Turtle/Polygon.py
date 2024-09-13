import turtle 
turtle.Screen().bgcolor("lavender")
turtle.Screen().setup(400,500)
p = turtle.Turtle()

n_sides = 6
angle = 360.0/n_sides
side_length = 80
p.color("purple")
p.speed(1)

for i in range(n_sides) :
    p.forward(side_length)
    p.right(angle)

turtle.done()