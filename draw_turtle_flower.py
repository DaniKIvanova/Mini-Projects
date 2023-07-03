import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("black")

    nate = turtle.Turtle()
    nate.shape("turtle")
    nate.color("yellow")

    for a in range(9):
        for b in range(4):
            nate.forward(100)
            nate.right(90)
        nate.right(160)

    window.exitonclick()

draw()
