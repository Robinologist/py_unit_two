#Setup & Defaults
import turtle
import random
turtle.hideturtle()
turtle.colormode(255)
turtle.speed(1)
turtle.showturtle()
pointsize=random.randrange(0, 7, 6)

turtle.tracer(0, 0)

#Settings Function
def GenerateSettings():
    global size
    global sides
    size=50
    sides=random.randrange(5,13)

#Color Function
def RandomColor():
    global R
    global G
    global B

    global R2
    global G2
    global B2

    R = random.randint(1,255)
    G = random.randint(1,255)
    B = random.randint(1,255)

    R2 = random.randint(1, 255)
    G2 = random.randint(1, 255)
    B2 = random.randint(1, 255)

#Pattern Function:
def CreatePattern():
    RandomColor()
    turtle.fillcolor(R, G, B)
    for x in range(sides):
        turtle.forward(size)
        turtle.left(360 / sides)
        turtle.begin_fill()
        for x in range(sides):
            turtle.fillcolor(R2, G2, B2)
            turtle.circle(pointsize)
            turtle.forward(size)
            turtle.left(360 / sides)
            turtle.left(360 / sides)
        turtle.end_fill()

#Make Patterns

for x in range(random.randint(3,9)):
    GenerateSettings()
    turtle.penup()
    turtle.goto(-size,0)
    turtle.goto( turtle.pos() + (0,-size*sides/6) )
    turtle.seth(-90)
    turtle.seth(0)
    turtle.pendown()
    turtle.hideturtle()
    turtle.penup()
    CreatePattern()

print("Size:", size)
print("Sides:", sides)
print("RGB  ==", R, G, B)
print("RGB2 ==", R2, G2, B2)

turtle.update()

turtle.exitonclick()