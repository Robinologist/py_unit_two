# Setup
import turtle
import math
import sys

#Intro
print("This program will calculate the slope between two lines;\n"
      "Just input the coordinates of two points and the slope will be calculated.\n"
      "Only non-0 integers will be accepted.\n")

# Variables
X1 = input("What is point 1's X value?\n")
Y1 = input("What is point 1's Y value?\n")
X2 = input("What is point 2's X value?\n")
Y2 = input("What is point 2's Y value?\n")
integers = 0
error = 0
Slope1 = 0
Slope2 = 0
Output = 0


# Functions
def TurtleFunction():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(X1 * 10, Y1 * 10)
    turtle.goto(X2 * 10, Y2 * 10)
    turtle.penup


def Error():
    global error
    error = 1
    print("Error: the two lines can not share X or Y values")


def MathFunction():
    global Slope1
    global Slope2
    global Output

    try: Slope1 = (Y1 - 0) / (X1 - 0)
    except: Error()
    else:
        try: Slope2 = (Y2 - Y1) / (X2 - X1)
        except: Error()
        else:
            Output = math.fabs(Slope1 - Slope2 / 1 + (Slope2 * Slope1))
            Output = math.atan(Output)
            Output = (Output * 180 / math.pi)


def CheckIntegers():
    try:
        global X1
        X1 = int(X1)
    except:
        print(X1, " is not a valid integer")
    else:
        try:
            global Y1
            Y1 = int(Y1)
        except:
            print(Y1, " is not a valid integer")
        else:
            try:
                global X2
                X2 = int(X2)
            except:
                print(X2, " is not a valid integer")
            else:
                try:
                    global Y2
                    Y2 = int(Y2)
                except:
                    print(Y2, " is not a valid integer")
                else:
                    global integers
                    integers = 1

CheckIntegers()
if integers == 1:
    MathFunction()
    if error == 0:
        TurtleFunction()
        print("The angle between the two lines is:",Output)
        turtle.exitonclick()
