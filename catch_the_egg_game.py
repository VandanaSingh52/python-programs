import pygame
import random
import math

# to initialize pygame
pygame.init()

# to create screen
screen = pygame.display.set_mode((800, 600))

# to create icon and title
icon = pygame.image.load('eggs.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Catch The Egg')

# background
backgroundImg = pygame.image.load('backgroundegg.jpg')


# basket
basketImg = pygame.image.load('basket.png')
basketX = 370
basketY = 480
basketX_change = 0


def basket(x, y):
    screen.blit(basketImg, (x, y))


# EGGS
eggImg = []
eggX = []
eggY = []
eggY_change = []

num_of_eggs = 10
for i in range(num_of_eggs):
    eggImg.append(pygame.image.load('eggsmall.png'))
    eggX.append(random.randint(0, 736))
    eggY.append(random.randint(-100, 100))
    eggY_change.append(0)


def egg(x, y, i):
    screen.blit(eggImg[i], (x, y))


# egg burst
burstImg = pygame.image.load('friedegg.png')
burstX = -100
burstY = -100


def burst(x, y):
    screen.blit(burstImg, (x, y))


# collision
def iscollision(eggX, eggY, basketX, basketY):
    distance = math.sqrt((math.pow(eggX - basketX, 2)) + (math.pow(eggY - basketY, 2)))
    if distance < 34:
        return True
    else:
        return False


# score

score_value = 0
font = pygame.font.Font('FreeSansBold.ttf', 32)
textX = 10
textY = 10
score_change = 1


def show_score(x, y):
    score = font.render('score :' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# egg crack
eggcrackImg = []
eggcrackX = []
eggcrackY = []
eggcrackY_change = []

num_of_eggcrack = 6

for i in range(num_of_eggcrack):
    eggcrackImg.append(pygame.image.load('eggcrack.png'))
    eggcrackX.append(random.randint(0, 736))
    eggcrackY.append(random.randint(0, 50))
    eggcrackY_change.append(0)


def eggcrack(x, y, i):
    screen.blit(eggcrackImg[i], (x, y))


def iscol(eggcrackX, eggcrackY, basketX, basketY):
    distance = math.sqrt((math.pow(eggcrackX - basketX, 2)) + (math.pow(eggcrackY - basketY, 2)))
    if distance < 34:
        return True
    else:
        return False


# game over
gameoverIMG = pygame.image.load('game-over.png')

# replay
replayImg = pygame.image.load('replay.png')

# loop of game
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                basketX_change = 0.6
            if event.key == pygame.K_LEFT:
                basketX_change = -0.6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                basketX_change = 0

    if basketX <= 0:
        basketX = 0
    if basketX > 736:
        basketX = 736

    basketX += basketX_change

    for i in range(num_of_eggs):
        eggY[i] += eggY_change[i]

        if eggY[i] >= 560:
            burstX = eggX[i]
            burstY = 545
            eggY[i] = 560

        if score_value >= 0 :
            num_of_eggs = 1
            num_of_eggcrack = 0
            eggY_change[i] = 0.3
        if score_value >= 4:
            num_of_eggs = 2
            num_of_eggcrack = 1
            eggY_change[i] = 0.3
            eggcrackY_change[i] = 0.2
        if score_value >= 10:
            num_of_eggs = 3
            num_of_eggcrack = 2
            eggY_change[i] = 0.4
            eggcrackY_change[i] = 0.2
        if score_value >= 18:
            num_of_eggs = 3
            num_of_eggcrack = 2
            eggY_change[i] = 0.4
            eggcrackY_change[i] = 0.3
        if score_value >= 27:
            num_of_eggs = 4
            num_of_eggcrack = 2
            eggY_change[i] = 0.5
            eggcrackY_change[i] = 0.3
        if score_value >= 35:
            num_of_eggs = 4
            num_of_eggcrack = 3
            eggY_change[i] = 0.5
            eggcrackY_change[i] = 0.4
        if score_value >= 45:
            num_of_eggs = 5
            num_of_eggcrack = 3
            eggY_change[i] = 0.6
            eggcrackY_change[i] = 0.4
        if score_value >= 75:
            num_of_eggs = 5
            num_of_eggcrack = 4
            eggY_change[i] = 0.6
            eggcrackY_change[i] = 0.5
        if score_value >= 100:
            num_of_eggs = 5
            num_of_eggcrack = 4
            eggY_change[i] = 0.6
            eggcrackY_change[i] = 0.6
        if score_value >= 120:
            num_of_eggs = 5
            num_of_eggcrack = 5
            eggY_change[i] = 0.6
            eggcrackY_change[i] = 0.6
            
        # collision
        collision = iscollision(eggX[i], eggY[i], basketX, basketY)
        if collision:
            eggX[i] = basketX
            eggY[i] = basketY
            eggX[i] = random.randint(0, 736)
            eggY[i] = random.randint(0, 100)
            score_value += score_change
        elif eggY[i] == 560:
            eggX[i] = random.randint(0, 736)
            eggY[i] = random.randint(0, 100)

        egg(eggX[i], eggY[i], i)
        burst(burstX, burstY)

    # eggcrack
    for i in range(num_of_eggcrack):
        eggcrackY[i] += eggcrackY_change[i]

        if eggcrackY[i] >= 560:
            burstX = eggcrackX[i]
            burstY = 545
            eggcrackY[i] = 560

        col = iscol(eggcrackX[i], eggcrackY[i], basketX, basketY)
        if col:
            screen.blit(gameoverIMG, (250, 100))
            screen.blit(replayImg, (350, 400))
            eggcrackX[i] = basketX
            eggcrackY[i] = basketY
            num_of_eggs = 0

        elif eggcrackY[i] == 560:
            eggcrackX[i] = random.randint(0, 736)
            eggcrackY[i] = random.randint(0, 50)

        eggcrack(eggcrackX[i], eggcrackY[i], i)
    
    basket(basketX, basketY)
    show_score(textX, textY)
    pygame.display.update()
