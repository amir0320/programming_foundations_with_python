import turtle

def draw_parallelogram(turtle, length):
    for unused in range(2):
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(120)

def draw_flower(color, length, speed, n):
    # customiz the window
    window = turtle.Screen()
    window.bgcolor("white")
    # customize the turtle
    ben = turtle.Turtle()
    ben.shape("turtle")
    ben.color("yellow")
    ben.shapesize(1.5,1.5,1.5)
    ben.speed(speed)
    ben.pencolor(color)
    ben.pensize(3)
    for unused in range(n):
        draw_parallelogram(ben, length)
        ben.right(360/n)
    ben.right(90)
    ben.forward(length * 3)
    window.exitonclick()
draw_flower("blue", 100, 10, 60)
