import pygame
import random
import math


width = 1600
height = 1000
drag = 0.95
El = 1.1#0.75
force = (math.pi,0)
n_balls = 100
selected_ball = None

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Billiard")

def create_color():
    r = random.randint(0,200)
    g = random.randint(0,200)
    b = random.randint(0,200)
    color = (r,g,b)
    if g >= 180 and b <= 60 and r <= b:
        create_color()
    return color

def Billiard():
    for i in range(10):
        size = 25
        if i == 0:
            x = width/2
            y = height/2
        if i == 1:
            x = width/2 + size + size/2
            y = height/2 - size - size/2
        if i == 2:
            x = width/2 + size + size/2
            y = height/2 + size + size/2
        if i == 3:
            x = width/2 + 3*size
            y = height/2 + 3*size
        if i == 4:
            x = width/2 + 3*size
            y = height/2
        if i == 5:
            x = width/2 + 3*size
            y = height/2 - 3*size
        if i == 6:
            x = width/2 + 4*size + size/2
            y = height/2 - 4*size - size/2
        if i == 7:
            x = width/2 + 4*size + size/2
            y = height/2 - 1*size - size/2
        if i == 8:
            x = width/2 + 4*size + size/2
            y = height/2 + size*1.5
        if i == 9:
            x = width/2 + 4*size + size/2
            y = height/2 + 4*size + size/2

        if i == 4:
            color = (10,10,10)
        else:
            color = create_color()
        ball = Ball((x,y),size,color,i)
        balls.append(ball)


def addV((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def find_rel_WB_M(wb, x, y):
    rel_WB_M = math.hypot(wb.x - x, wb.y - y)
    if rel_WB_M >= wb.size:
        return wb
    else:
        return None


'''
def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        tangent = math.atan2(dy, dx)
        angle = 0.5 * math.pi + tangent

        angle1 = 2*tangent - p1.angle
        angle2 = 2*tangent - p2.angle
        speed1 = p2.speed*El
        speed2 = p1.speed*El

        (p1.angle, p1.speed) = (angle1, speed1)
        (p2.angle, p2.speed) = (angle2, speed2)

        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)
        p2.x -= math.sin(angle)
        p2.y += math.cos(angle)
'''


def collide(b1, b2):
    if b1.id != b2.id:

        dx = b1.x - b2.x
        dy = b1.y - b2.y

        dist = math.hypot(dx, dy)
        if dist <= b1.size + b2.size:
            tan = math.atan2(dy, dx)
            angle = 0.5 * math.pi + tan

            m = random.uniform(0.9,1.2)
            n = random.uniform(0.9,1.2)

            angle1 = (0.5*math.pi - tan)
            angle2 = - angle1

            speed1 = ((b1.size*m - b2.size*n) * b1.speed + (b2.size*n * b2.speed))/(b1.size*m + b2.size*n)
            speed2 = (b1.size*m * b1.speed - (b1.size*m - b2.size*n)* b2.speed)/(b1.size*m + b2.size*n)

            speed1 *= El
            speed2 *= El

            (b1.angle, b1.speed) = (angle1, math.sqrt(speed1**2)*El)
            (b2.angle, b2.speed) = (angle2, math.sqrt(speed2**2)*El)

            ov = 0.5*(b1.size + b2.size - dist+1)

            b1.x += math.sin(angle)*ov
            b1.y -= math.cos(angle)*ov
            b2.x -= math.sin(angle)*ov
            b2.y += math.cos(angle)*ov


class WBall():
    def __init__(self,(x,y)):
        self.x = x
        self.y = y
        self.size = 25
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, (220,220,220), (int(self.x), int(self.y)), self.size,0)

    def move(self):
        (self.angle, self.speed) = addV((self.angle, self.speed), force)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

        self.speed *= drag

    def bounce(self):
        if self.x + 30 > width - self.size:
            self.x = width - 30 - self.size
            self.angle = - self.angle
            self.speed *= El

        elif self.x - 30 < self.size:
            self.x = self.size + 30
            self.angle = - self.angle
            self.speed *= El

        if self.y + 30 > height - self.size:
            self.y = height - 30 - self.size
            self.angle = math.pi - self.angle
            self.speed *= El

        elif self.y - 30 < self.size:
            self.y = self.size + 30
            self.angle = math.pi - self.angle
            self.speed *= El

    def collide(self, other):

        dx = self.x - other.x
        dy = self.y - other.y

        dist = math.hypot(dx, dy)
        if dist < self.size + other.size:
            tan = math.atan2(dy, dx)

            m = random.uniform(1,1.5)
            n = random.uniform(1,1.5)

            angle1 = (0.5*math.pi - tan)
            angle2 = - angle1

            speed1 = ((self.size*m - other.size*n) * self.speed + (other.size*n * other.speed))/(self.size*m + other.size*n)
            speed2 = (self.size*m * self.speed - (self.size*m - other.size*n)* other.speed)/(self.size*m + other.size*n)

            speed1 *= El
            speed2 *= El

            (self.angle, self.speed) = (angle1, math.sqrt(speed1**2)*El)
            (other.angle, other.speed) = (angle2, math.sqrt(speed2**2)*El)

            ov = 0.5*(self.size + other.size - dist+1)
            af = 0.5 * math.pi + tan

            self.x += math.sin(af)*ov
            self.y -= math.cos(af)*ov
            other.x -= math.sin(af)*ov
            other.y += math.cos(af)*ov



class Ball():
    def __init__(self, (x, y), size, color, id):
        self.x = x
        self.y = y
        self.size = size
        self.colour = color
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.id = id

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        (self.angle, self.speed) = addV((self.angle, self.speed), force)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

        self.speed *= drag

    def bounce(self):
        if self.x + 30 > width - self.size:
            self.x = width - 30 - self.size
            self.angle = - self.angle
            self.speed *= El

        elif self.x - 30 < self.size:
            self.x = self.size + 30
            self.angle = - self.angle
            self.speed *= El

        if self.y + 30 > height - self.size:
            self.y = height - 30 - self.size
            self.angle = math.pi - self.angle
            self.speed *= El

        elif self.y - 30 < self.size:
            self.y = self.size + 30
            self.angle = math.pi - self.angle
            self.speed *= El


class Hole:
    def __init__(self, x, y):
        self.size = 40
        self.x = x + self.size/2 + 10
        self.y = y + self.size/2 + 10
        self.color = (0,0,0)

    def display(self):
        pygame.draw.circle(screen,self.color,(self.x, self.y) , self.size,0)

    def checkfall(self,b):
        dx = self.x - b.x
        dy = self.y - b.y

        dist = math.hypot(dx, dy)
        if dist <= b.size + self.size/2:
            if b in wballs:
                b.speed = 0
                b.x = width/4
                b.y = height/2
            elif b.colour == (10,10,10):
                global running
                running = False
            else:
                balls.remove(b)



def border():
    pygame.draw.rect(screen, (180,180,180), (0, 0, width, 30))
    pygame.draw.rect(screen, (180,180,180), (0, 0, 30, height))
    pygame.draw.rect(screen, (180,180,180), (width - 30, 0, width, height))
    pygame.draw.rect(screen, (180,180,180), (0, height - 30, width, height))

def create_holes():

    hole1 = Hole(15, 15)
    hole2 = Hole(width/2 - hole1.size, 0 )
    hole3 = Hole(width - 15 - hole1.size/2 - 30 - 5, 15 )
    hole4 = Hole(15, height - 30 - 5 - 15 - hole1.size/2 )
    hole5 = Hole(width/2 - hole1.size/2, height - 30 - 5 - hole1.size/2 )
    hole6 = Hole(width - 15 - hole1.size/2 - 30 - 5, height - 15 - 30 - 5 - hole1.size/2 )

    holes.append(hole1)
    holes.append(hole2)
    holes.append(hole3)
    holes.append(hole4)
    holes.append(hole5)
    holes.append(hole6)

holes = []

def create_balls():
    for i in range(n_balls):
        size = random.randint(20,50)
        x = random.randrange(size,width-size)
        y = random.randrange(size,height-size)
        color = create_color()
        ball = Ball((x,y),size,color,i)
        balls.append(ball)
        ball.speed = random.randrange(5,15)
        ball.angle = random.uniform(0,2*math.pi)

balls = []

'''
for n in range(n_of_balls):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)

    ball = Ball((x, y), size)
    ball.speed = 0
    ball.angle = random.uniform(0, math.pi*2)

    balls.append(ball)
'''




wball = WBall((width/4,height/2))
wballs = []
wballs.append(wball)

Billiard()
create_holes()

#create_balls()


running = True
while running:
    clock.tick(60)

    screen.fill((50,190,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_ball = find_rel_WB_M(wball, mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_ball = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if selected_ball:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_ball.x
        dy = mouseY - selected_ball.y

        selected_ball.angle = (math.atan2(dy, dx) - 0.5*math.pi)
        selected_ball.speed = math.hypot(dx, dy) * 0.1

    if selected_ball == None and wball.speed <= 0.5:
            t = pygame.mouse.get_pos()
            y = wball.y - t[1]
            x = wball.x - t[0]
            ds = math.hypot(x,y)
            tan = math.atan2(x,y)
            hx = wball.x + ds/2 * math.sin(tan)
            hy = wball.y + ds/2 * math.cos(tan)
            pygame.draw.line(screen,(220,220,220),(wball.x,wball.y),(hx,hy),6)
    border()

    for i, ball in enumerate(balls):
        ball.move()
        ball.bounce()
        wball.collide(ball)
        for n, hole in enumerate(holes):
            hole.checkfall(ball)
            hole.checkfall(wball)
        for x, ball2 in enumerate(balls):
            collide(ball, ball2)
        ball.display()

    for i, hole in enumerate(holes):
        hole.display()


    wball.display()
    wball.move()
    wball.bounce()

    pygame.display.flip()
    if balls == None:
        running = False

pygame.quit()
