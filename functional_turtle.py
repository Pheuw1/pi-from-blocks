import turtle
import random
t = turtle.Pen()
t.speed(0)
t.width(3)

pink = (230, 155, 75)
teal = (0, 128, 128)

colorlist = ["red", "green", "blue", "orange", "yellow", "pink", "teal"]
anglelist = [7, 15, 30, 45, 90, 153, 180, 270, 360]

def square(size):
    t.up()
    t.goto(random.randrange(-400, 400), random.randrange(-400, 400))
    t.down()
    t.left(random.choice(anglelist))
    col = random.choice(colorlist)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.left(90)
    t.end_fill()
    t.fillcolor(col)

def triangle(size):
    t.up()
    t.goto(random.randrange(-400, 400), random.randrange(-400, 400))
    t.down()
    t.left(random.choice(anglelist))
    col = random.choice(colorlist)
    t.begin_fill()
    for i in range(3):
        t.fd(size)
        t.left(120)
    t.end_fill()
    t.fillcolor(col)

def raT(size):
    x = random.randrange(-400, 400)
    y = random.randrange(-400, 400)
    t.up()
    t.goto(x, y)
    t.down()
    t.left(random.choice(anglelist))
    col = random.choice(colorlist)
    t.begin_fill()
    t.fd(size)
    t.left(90)
    t.fd(size/2)
    t.left(60)
    t.goto(x, y)
    t.end_fill()
    t.fillcolor(col)

def Hexagon(size):
    t.up()
    t.goto(random.randrange(-400, 400), random.randrange(-400, 400))
    t.down()
    t.left(random.choice(anglelist))
    col = random.choice(colorlist)
    t.begin_fill()
    for i in range(6):
        t.fd(size/2)
        t.left(60)
    t.end_fill()
    t.fillcolor(col)

for i in range(100):

    square(random.randrange(50, 300))

    triangle(random.randrange(80,240))

    raT(random.randrange(50+i, 300+i))

    Hexagon(random.randrange(50, 300))

    t.left(random.choice(anglelist))
    t.up()
    t.goto(random.randrange(-400, 400), random.randrange(-400, 400))
    t.down()
    col = random.choice(colorlist)
    t.begin_fill()
    t.left(random.choice(anglelist))
    t.circle(random.randrange(25, 300), random.choice(anglelist))
    t.end_fill()
    t.fillcolor(col)
