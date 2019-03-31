import pygame
from pygame.locals import *
from math import *
import time
import random

WIDTH = 1000
HEIGHT = 1000



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Double pendulum")
clock = pygame.time.Clock()

L1 = 250.0;
L2 = 250.0;
m1 = 2
m2 = 2
a1 = random.uniform(-pi, pi);
a2 = random.uniform(-pi, pi);
a1v = 0;
a2v = 0;
g = 9.8;

def angle1():
    global a1
    global a1v
    a1a = ((-g *(( 2 * (m1 + m2)) * sin(a1)) - (m2*g *sin( a1 - (2 * a2) )) - (2 * sin(a1 - a2)) * m2 *((a2v * a2v) * L2) + ((a1v*a1v) * L1*cos(a1 - a2))) / (L1 * (((2*m1) + m2) - ((m2 * cos((2 * a1) - (2 * a2)))))))
    a1v += a1a/(FPS/15)
    a1 += a1v/(FPS/30)
    print(a1a)

def angle2():
    global a2
    global a2v
    a2a = (((2 * sin(a1 - a2)) * ((((a1v*a1v))*L1 * (m1 + m2)) + (g*(m1 + m2)*cos(a1)) + (a2v*a2v)*L2*m2*cos(a1 - a2))) / (L2 * (((2*m1) + m2) - ((m2 * cos((2 * a1) - (2 * a2)))))))
    a2v += a2a/(FPS/15)
    a2 += a2v/(FPS/30)
    print(a2a)

def refresh():
    global a1
    global a2
    ticks = pygame.time.get_ticks()
    if ticks >= 5000:
        a1 = random.uniform(-pi, pi);
        a2 = random.uniform(-pi, pi);

def trace():
    nx2 = x1 + int(L2 * sin(a2))
    ny2 = y1 + int(L2 * cos(a2))
    x2 = x1 + int(L2 * sin(a2))
    y2 = y1 + int(L2 * cos(a2))
    list = [(nx2,ny2), (x2,y2)]
    pygame.draw.lines(screen, BLACK, False, list, 3)
    pygame.Surface.lock(screen)

def fs():
    pygame.display.toggle_fullscreen()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fs()
    x1 = WIDTH/2 + int(L1 * sin(a1))
    y1 = HEIGHT/2 + int(L1 * cos(a1))
    x2 = x1 + int(L2 * sin(a2))
    y2 = y1 + int(L2 * cos(a2))
    angle1()
    angle2()
    screen.fill(WHITE)
    pygame.draw.aaline(screen, BLACK, (WIDTH/2 , HEIGHT/2), (x1, y1), 0)
    pygame.draw.circle(screen, BLACK, (x1, y1), m1*8, 0)
    pygame.draw.aaline(screen, BLACK, (x1, y1), (x2, y2), 0)
    pygame.draw.circle(screen, BLACK, (x2, y2), m2*8, 0)
    pygame.display.update()
pygame.quit()
