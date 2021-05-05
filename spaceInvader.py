import pygame, sys, random

#screen
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Space Invader')
background = pygame.image.load('img/bg.jpg')

#player
player = pygame.image.load('img/space-invaders.png') # Icon made by freepik from www.flaticon.com
pygame.display.set_icon(player)
playerX = 608
playerY = 550

#enemy
enemy_num = 8
class Enemy:
    def __init__(self):
        self.img = pygame.image.load('img/monster.png') # Icon made by Smashicons from www.flaticon.com
        self.x = random.randint(0, 1248)
        self.y = random.randint(5, 80)
        self.step = 0.3
enemies = []
for i in range(enemy_num):
    enemies.append(Enemy())

#bullet
class Bullet:
    def __init__(self):
        self.img = pygame.image.load('img/bullet.png') # Icon made by Smashicons from www.flaticon.com
        self.x = playerX + 20
        self.y = playerY - 28
        self.step = 0.5
bullets = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        playerStep = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerStep = 0.5
            elif event.key == pygame.K_LEFT:
                playerStep = -0.5
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet())

    screen.blit(background, (0,0))

    screen.blit(player, (playerX, playerY))
    playerX += playerStep
    if playerX > 1216:
        playerX = 1216
    if playerX < 0:
        playerX = 0

    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        if e.x > 1248 or e.x < 0:
            e.step *= -1
            e.y += 64
        e.x += e.step

    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)

    pygame.display.update()
