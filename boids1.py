import pygame
from pygame import gfxdraw
import math
import random

Height = 1100
Width = 1800
n_of_boids = 50
display = pygame.display.set_mode((Width,Height))
clock = pygame.time.Clock()

class Boid():
    def __init__(self,(x,y),speed,id):
        self.x = x
        self.y = y
        self.speed = speed
        self.orientation = random.uniform(0,2*math.pi)
        self.size = 10
        self.perception = 150
        self.see_other = False
        self.close = False
        self.too_close = None
        self.urgent = speed * 1.5
        self.id = id

    def draw(self):
        x1 = self.x + math.cos(self.orientation) * self.size
        y1 = self.y - math.sin(self.orientation) * self.size
        x2 = self.x + math.cos(self.orientation - 2*math.pi/3) * self.size * 2/3
        y2 = self.y - math.sin(self.orientation - 2*math.pi/3) * self.size * 2/3
        x3 = self.x + math.cos(self.orientation + 2*math.pi/3) * self.size * 2/3
        y3 = self.y - math.cos(self.orientation + 2*math.pi/3) * self.size * 2/3
        pygame.gfxdraw.trigon(display, int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), (90,90,240))

    def move(self):
        self.x += math.cos(self.orientation) * self.speed
        self.y -= math.sin(self.orientation) * self.speed

        if self.x > Width:
            self.x = 0
        if self.x < 0:
            self.x = Width
        if self.y > Height:
            self.y  = 0
        if self.y < 0:
            self.y = Height

    def explore(self):
        if self.see_other == False:
            self.orientation += random.uniform(-0.05,0.05)

    def notice(self,other):
        if self.id != other.id:
            ds = math.hypot((self.x - other.x),(self.y - other.y))

            if ds <= self.size + self.perception:
                self.see_other = True
            else:
                self.see_other = False

            if ds <= self.size + 100:
                self.close = True
            else:
                self.close = False

            if ds <= self.size + 30:
                self.too_close = True
            else:
                self.too_close = False

            if self.see_other == False:
                self.close = False
            if self.close == False:
                self.too_close = False

    def allign_with_other(self,other):
        if self.close == True and self.id != other.id:

            gspeed = other.speed/self.speed * self.speed
            lspeed = self.speed/other.speed * other.speed
            if self.speed > other.speed:
                (self.speed,other.speed) = (lspeed,gspeed)
            else:
                (self.speed,other.speed) = (lspeed,lspeed)

            ro = self.orientation - other.orientation
            if ro >= 0:
                self.orientation -= ro * 4/math.hypot((self.x - other.x),(self.y - other.y))
                other.orientation += ro * 4/math.hypot((self.x - other.x),(self.y - other.y))
            elif ro < 0:
                self.orientation += ro * 4/math.hypot((self.x - other.x),(self.y - other.y))
                other.orientation -= ro * 4/math.hypot((self.x - other.x),(self.y - other.y))


    "this function works somewhat. is supposed to avoid self and other from colliding. problems with orientation"
    def avoid_other(self,other):
        if self.too_close == True and self.id != other.id:

            dx = self.x - other.x
            dy = self.y - other.y
            ds = math.hypot(dx,dy)

            if self.speed != self.urgent or other.speed != other.urgent:
                self.speed = self.urgent
                other.speed = other.urgent

            so = math.atan2(dy,dx)
            ss = math.atan2(other.y - self.y,other.x - self.x)

            '''
            if other.orientation <= so - so * 2/ds:
                other.orientation -= so * 0.5/ds
            elif other.orientation >= so + so * 2/ds:
                other.orientation -= so * 0.5/ds
            '''

            if self.orientation <= ss - ss * 2/ds:
                self.orientation += ss * 0.5/ds
            elif other.orientation >= ss + ss* 2/ds:
                self.orientation += ss * 0.5/ds

        elif self.too_close == False and (self.speed == self.urgent or other.speed == other.urgent):
            self.speed = self.urgent/1.5
            other.speed = other.urgent/1.5

def RESPEC_MAH_OTORITEH(b,list):
    if b.see_other == True and b.close == False:
        x = b.x
        y = b.y
        for i, b2 in enumerate(list):
            if b.id != b2.id and (math.hypot((b2.x - b.x),(b2.y - b.y)) <= b.perception*2):
                x += (b.x - b2.x)
                y += (b.y - b2.y)
                #pygame.draw.line(display,(255,255,255),(int(b.x),int(b.y)),((b2.x),(b2.y)),1)
                #b2.orientation -= 0.01 * math.atan2((b2.y - b.y),(b2.x - b.x))
        b.orientation += 0.02 * math.atan2((b.y - y),(b.x - x))

boids = []
for i in range(n_of_boids):
    x = random.randrange(0,Width)
    y = random.randrange(0, Height)
    speed = random.uniform(5, 10)
    boid = Boid((x,y),speed,i)
    boids.append(boid)

running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    display.fill((50,50,50))

    for x, b in enumerate(boids):
        b.draw()
        b.move()
        for y, b2 in enumerate(boids):
            b.notice(b2)
            b.allign_with_other(b2)
            b.avoid_other(b2)
            RESPEC_MAH_OTORITEH(b,boids)
    pygame.display.flip()

pygame.quit()
