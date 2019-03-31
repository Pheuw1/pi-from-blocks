
import pygame
import random
import os
import pyganim
import math

WIDTH = 960
HEIGHT = 650
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

project_folder = os.path.dirname(__file__)
asset_folder = os.path.join(project_folder, "assets")
sound_folder = os.path.join(project_folder, "sound")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Player_img, (40, 60))
        self.rect = self.image.get_rect()
        self.radius = 21
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def rotate(Bullet):
            if Bullet.speedx > 0:
                Bullet.rot = 180
            if Bullet.speedy > 0:
                Bullet.rot = 270
            if Bullet.speedy < 0:
                Bullet.rot = 90

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x +=self.speedx

        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.y +=self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


    def shootw(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        Bullet.speedx = 0
        Bullet.speedy = -30
        rotate(Bullet)


    def shoots(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(bullet)
        bullets.add(bullet)
        Bullet.speedx = 0
        Bullet.speedy = 30
        rotate(Bullet)


    def shoota(self):
        bullet = Bullet(self.rect.left, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
        Bullet.speedx = -30
        Bullet.speedy = 0
        rotate(Bullet)


    def shootd(self):
        bullet = Bullet(self.rect.right, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
        Bullet.speedx = 30
        Bullet.speedy = 0
        rotate(Bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(asset_folder, "young_brod.png"))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        self.speedy = random.randrange(-4, 4)
        self.speedx = random.randrange(-4, 4)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.speedx = random.randrange(-4, 4)
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedy = random.randrange(-4, 4)
        if self.rect.bottom < 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.speedx = random.randrange(-4, 4)
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedy = random.randrange(-4, 4)
        if self.rect.right > WIDTH - 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.speedx = random.randrange(-4, 4)
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedy = random.randrange(-4, 4)
        if self.rect.left < 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.speedx = random.randrange(-4, 4)
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedy = random.randrange(-4, 4)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(Bullet_img, (30, 30))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rot = 0
        self.rect.centery = y
        self.rect.centerx = x
        self.last_update = pygame.time.get_ticks()


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > HEIGHT:
            self.kill()
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > WIDTH:
            self.kill()


def rotate(Bullet):
    if Bullet.speedx > 0:
        Bullet.rot = 180
    if Bullet.speedy > 0:
        Bullet.rot = 270
    if Bullet.speedy < 0:
        Bullet.rot = 90



pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Look at 'im goooooo")
clock = pygame.time.Clock()


background = pygame.image.load(os.path.join(asset_folder, "sticky_bg.png"))
background_rect = background.get_rect()
Bullet_img = pygame.image.load(os.path.join(asset_folder, "no_thanks.png"))
Player_img = pygame.image.load(os.path.join(asset_folder, "brod.png"))

#self.image.set_colorkey(color)


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.shootw()
            if event.key == pygame.K_s:
                player.shoots()
            if event.key == pygame.K_a:
                player.shoota()
            if event.key == pygame.K_d:
                player.shootd()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        running = True

    screen.fill(WHITE)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
