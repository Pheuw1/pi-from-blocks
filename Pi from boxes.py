import pygame
import math


WIDTH = 800
HEIGHT = 550
FPS = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#ke = 1/2(smass * sspeedx) + 1/2(bmass * bspeedx)
#Ke = 1/2(Sbox.mass * Sbox.speedx) + 1/2(Bbox.mass * Bbox.speedx)
#p = smass * sspeedx + bmass * bspeedx
#P = Sbox.mass * Sbox.speedx + Bbox.mass * Bbox.speedx




class Bbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 50
        self.rect.right = WIDTH - 300
        self.speedx = 1
        self.mass = 1 * (99.9)

    def update(self):
        self.rect.x -= self.speedx



class Sbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 50
        self.rect.left = 100
        self.speedx = 0
        self.mass = 1

    def update(self):
        self.rect.x -= self.speedx



bigboi = pygame.sprite.Group()
smallboi = pygame.sprite.Group()
Bbox = Bbox()
Sbox = Sbox()
bigboi.add(Bbox)
smallboi.add(Sbox)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

col = 0


running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bsbois = pygame.sprite.groupcollide(bigboi, smallboi, False, False)
    if bsbois:
        nsspeedx = (((Sbox.mass - Bbox.mass)/(Sbox.mass + Bbox.mass)) * (Sbox.speedx)) + ((2*Bbox.mass) / (Bbox.mass + Sbox.mass)) * Bbox.speedx
        nbspeedx = (((Bbox.mass - Sbox.mass)/(Bbox.mass + Sbox.mass)) * (Bbox.speedx)) + ((2*Sbox.mass) / (Bbox.mass + Sbox.mass)) * Sbox.speedx
        Sbox.speedx = nsspeedx
        Bbox.speedx = nbspeedx
        if Sbox.rect.right > Bbox.rect.left:
            Bbox.rect.left = Sbox.rect.right
        print(nsspeedx)
        print(nbspeedx)
        col = col + 1
        print(col)

    if Sbox.rect.left <= 0:
        Sbox.rect.left = 1
        Sbox.speedx = -Sbox.speedx
        col = col + 1
        print(col)
        print(Sbox.speedx)


    bigboi.update()
    smallboi.update()

    screen.fill(BLACK)
    bigboi.draw(screen)
    smallboi.draw(screen)
    pygame.display.flip()

pygame.quit()
