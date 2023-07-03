import turtle as tt

tt.Screen().bgcolor("white")
tt.pensize(2)
tt.speed(10)

for _ in range(6):
    for color in ["blue", "red", "purple", "green", "yellow", "cyan", "pink", "magenta", "orange"]:
        tt.color(color)
        tt.circle(100)
        tt.left(10)

    tt.hideturtle()

tt.done()

