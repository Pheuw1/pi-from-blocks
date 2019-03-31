import turtle

t = turtle.Pen()
t.shape("turtle")
t.width(5)
t.speed(0)
for i in range(4):
    t.fd(100)
    t.left(90)

t.reset()
t.width(5)
t.speed(0)
for i in range(8):
    t.fd(100)
    t.left(225)

for i in range(5):
    print(i)

t.reset()
t.width(5)
t.speed(0)
for i in range (30):
    t.fd(10 * i)
    t.left(90)


t.reset()
t.width(3)
t.speed(0)
for i in range(150):
    t.circle(i*2)
    t.left(5)

t.reset()
t.width(1)
t.speed(0)
t.color("red")
for i in range(50):
    t.begin_fill()
    t.fd(i * 3)
    t.circle(i * 3, 90)
    t.end_fill()
    t.right(20)
