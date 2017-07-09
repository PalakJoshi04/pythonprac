# draw graphic pentagon design
import turtle
sides = 5
turtle.color('red')
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360/sides)
    for steps in range(sides):
        turtle.forward(50)
        turtle.left(360/sides)
        for steps in range(sides):
            turtle.forward(10)
            turtle.right(360/sides)
