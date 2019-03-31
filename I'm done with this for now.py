import pygame
import math
from decimal import Decimal


WIDTH = 800
HEIGHT = 550
FPS = 100000000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#ke = 1/2(smass * sspeedx) + 1/2(bmass * bspeedx)
#Ke = 1/2(Sbox.mass * Sbox.speedx) + 1/2(Bbox.mass * Bbox.speedx)
#p = smass * sspeedx + bmass * bspeedx
#P = Sbox.mass * Sbox.speedx + Bbox.mass * Bbox.speedx
#TRY FUNCTION



#n = desired digits of pi -1
n = 2

def elastic(Sspeedx, Bspeedx):
    Bspeedx = ((Bbox.mass - Sbox.mass) * Bbox.speedx + Decimal('2.0') * Sbox.mass * Sbox.speedx)/(Bbox.mass + Sbox.mass)
    Sspeedx = (Decimal('2.0') * Bbox.mass * Bbox.speedx - (Bbox.mass - Sbox.mass)* Sbox.speedx)/(Bbox.mass + Sbox.mass)
    Bbox.speedx = Bspeedx
    Sbox.speedx = Sspeedx
    Bbox.rect.left = Sbox.rect.right + 0.01
    if Bbox.rect.left > Sbox.rect.right:
        Bbox.rect.left = Bbox.rect.left + 0.01
class Bbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((250, 250))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 50
        self.rect.right = WIDTH - 300
        self.speedx = Decimal('-1.0')
        self.mass = 1 * (100**n)

    def update(self):
        self.rect.x += self.speedx
        self.speedx = self.speedx

class Sbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 50
        self.rect.left = 100
        self.speedx = Decimal('0.0')
        self.mass = Decimal('1.0')
    def update(self):
        self.rect.x += self.speedx
        self.speedx = self.speedx

bigboi = pygame.sprite.Group()
smallboi = pygame.sprite.Group()
Bbox = Bbox()
Sbox = Sbox()
bigboi.add(Bbox)
smallboi.add(Sbox)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pi from box collisions")
clock = pygame.time.Clock()

col = 0


running = True
while running:

    clock.tick(FPS)

    collide = pygame.sprite.groupcollide(bigboi, smallboi, False, False)

    if collide:
        elastic(Sbox.speedx, Bbox.speedx)
        print(Bbox.speedx)
        print(Sbox.speedx)
        col = col + 1.0
        print(col)

    elif Sbox.rect.left <=0:
        Sbox.speedx = -Sbox.speedx
        Sbox.rect.left = 1
        col = col + 1
        print(col)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bigboi.update()
    smallboi.update()

    screen.fill(BLACK)
    bigboi.draw(screen)
    smallboi.draw(screen)
    pygame.display.flip()

pygame.quit()
