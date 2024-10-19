import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("light blue")

def circles(color, radius):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

t.up()
t.setpos(-60, 110)
t.down
circles('brown', 24)

t.up()
t.setpos(60, 110)
t.down()
circles('brown', 24)

t.up()
t.setpos(0, -90)
t.down()
circles('brown', 110)

t.up()
t.setpos(-28, 35)
t.down
circles('black', 13)

t.up()
t.setpos(28, 35)
t.down()
circles('black', 13)

t.up()
t.setpos(-25, 44)
t.down()
circles('white', 5)

t.up()
t.setpos(25, 44)
t.down()
circles('white', 5)

t.up()
t.setpos(0, 10)
t.down
circles('black', 9)

t.up()
t.setpos(0, 10)
t.down()
t.right(90)
t.circle(15, 180)
t.up()
t.setpos(0, 10)
t.down()
t.left(360)
t.circle(15, -180)
t.hideturtle()