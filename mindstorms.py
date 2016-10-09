import turtle

def draw_turtles():
    window = turtle.Screen()
    window.bgcolor("yellow")
    amir = turtle.Turtle()
    amir.shape("turtle")
    amir.color("green")
    amir.shapesize(3,3,3)
    amir.speed(1)
    amir.pencolor("white")
    amir.pensize(5)
    for unuesd in range(4):
        amir.forward(100)
        amir.right(90)

    rod = turtle.Turtle()
    rod.shape("turtle")
    rod.color("green")
    rod.shapesize(2,2,2)
    rod.speed(1)
    rod.pencolor("white")
    rod.pensize(5)
    rod.circle(100)

    me = turtle.Turtle()
    me.shape("turtle")
    me.color("green")
    for unused in range(3):
        me.backward(100)
        me.right(120)
    window.exitonclick()
draw_turtles()
