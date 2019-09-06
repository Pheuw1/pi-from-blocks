import pygame
import math
import random

Width = 1800
Height = 1000
display = pygame.display.set_mode((Width,Height))
clock = pygame.time.Clock()

G = 6.7 * (10**-11)
ms = 10**14
ds = 10**16
El = 1

def addVs((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle  = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)

def create_color():
    r = random.randint(0,200)
    g = random.randint(0,200)
    b = random.randint(0,200)
    color = (r,g,b)

    return color

class Celestial():
    def __init__(self,(x,y),speed,angle,color,size,id):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.color = color
        self.size = size
        self.id = id

    def accelerate(self, V):
        (self.angle, self.speed) = addVs((self.angle, self.speed), V)

    def move(self):
        self.x += math.sin(self.angle) * (self.speed/ds)
        self.y -= math.cos(self.angle) * (self.speed/ds)

    def draw(self):
        pygame.draw.circle(display, self.color, (int(self.x),int(self.y)), self.size)
        #pygame.draw.aaline(display,(255,255,255),(self.x,self.y),(self.x + math.sin(self.angle) * 10, self.y -math.cos(self.angle) * 10))
        if self in Celestials and (self.x > Width + self.size or self.x < -self.size or self.y > Height + self.size or self.y < -self.size):
            Celestials.remove(self)
            create_random_Celestials(1)

    def attract(self,other):
        if self.id != other.id:
            dx = self.x - other.x
            dy = self.y - other.y

            r = math.hypot(dx,dy)
            tan = math.atan2(dy, dx)

            if r >= self.size:
                a = (G*(self.size*ms + other.size*ms)/(r**2))/self.size*ms
                self.accelerate((tan - 0.5*math.pi,a))

            #if self.id == 1:
                #pygame.draw.aaline(display, (255,255,255), (self.x,self.y), (other.x,other.y))

    def merge(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        ds = math.hypot(dx,dy)
        if self.id != other.id and ds < self.size + other.size/2:

            length = (self.size*ms * self.speed - (self.size*ms - other.size*ms)* other.speed)/(self.size*ms + other.size*ms)
            x  = math.sin(other.angle) + math.sin(self.angle)
            y  = math.cos(other.angle) + math.cos(self.angle)
            angle = 0.5 * math.pi - math.atan2(y,x)

            if self.size <= other.size:
                other.size += int(self.size/(other.size*0.2))
                other.angle,other.speed = angle,length*0.3
                other.color = ((self.color[0]+ other.color[0])/2,(self.color[1] + other.color[1])/2,(self.color[2] + other.color[2])/2)

                if self in Celestials:
                    Celestials.remove(self)
                    #create_random_Celestials(1)

    def collide(self, other):

        dx = self.x - other.x
        dy = self.y - other.y

        dist = math.hypot(dx, dy)
        if dist < self.size + other.size:
            tan = math.atan2(dy, dx)

            m = ms#random.uniform(1,1.5)
            n = ms#random.uniform(1,1.5)

            angle1 = (0.5*math.pi - tan)
            angle2 = - angle1

            speed1 = ((self.size*m - other.size*n) * self.speed + (other.size*n * other.speed))/(self.size*m + other.size*n)
            speed2 = (self.size*m * self.speed - (self.size*m - other.size*n)* other.speed)/(self.size*m + other.size*n)

            speed1 *= El
            speed2 *= El

            (self.angle, self.speed) = (angle1, math.sqrt(speed1**2)*El)
            (other.angle, other.speed) = (angle2, math.sqrt(speed2**2)*El)

            ov = 0.5*(self.size + other.size - dist)
            af = 0.5 * math.pi + tan

            self.x += math.sin(af)*ov
            self.y -= math.cos(af)*ov
            other.x -= math.sin(af)*ov
            other.y += math.cos(af)*ov

Celestials = []

def create_random_Celestials(n):
    for i in range(n):
        size = 10#random.randrange(3)
        x = random.randrange(size,Width-size)
        y = random.randrange(size,Height-size)
        speed = 0#random.uniform(0,4)*ds
        angle = random.uniform(0,math.pi*2)
        color = create_color()

        celestial = Celestial((x,y),speed,angle,color,size,i)
        Celestials.append(celestial)


create_random_Celestials(10)

running = True
while running:
    clock.tick(160)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                create_random_Celestials(1)

    display.fill((20,20,20))

    for i, c in enumerate(Celestials):
        c.move()
        c.draw()
        for j, c2 in enumerate(Celestials):
            c.attract(c2)
            #c.merge(c2)
            c.collide(c2)


    pygame.display.flip()

pygame.quit()
