import pygame
import random

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370
background_width = 1024

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))

def runGame():
    global gamepad, clock, aircraft, background1, background2
    global bat, fires, bullet

    crashed = False
    x = pad_width * 0.05
    y = pad_height * 0.8
    xbg1 = 0
    xbg2 = 0
    y_change = 0
    bulletxy = []
    bat_x = pad_width
    bat_y = random.randrange(0, pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0, pad_height)

    random.shuffle(fires)
    fire = fires[0]

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
            if event.type == pygame.KEYUP:
                if  event.key == pygame.K_DOWN:
                    y_change = 0
                elif event.key == pygame.K_LEFT:
                    bullet_x = x
                    bullet_y = y
                    bulletxy.append([bullet_x, bullet_y])


        xbg1 -= 5
        xbg2 -= 5

        y += y_change

        bat_x-=7
        if bat_x <= 0:
            bat_x = pad_width
            bat_y = random.randrange(0, pad_height)

        if fire_x == None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)
            random.shuffle(fires)
            fire = fires[0]

        if xbg1 == -background_width:
            xbg1 = background_width

        if xbg2 == background_width:
            xbg2 = background_width

        y+=2



        for p in range(0, len(bulletxy)):
            if bulletxy[p][0] >= bat_x and bulletxy[p][0] <= bat_x+50 and bulletxy[p][1] >= bat_y and bulletxy[p][1] <= bat_y + 50:
                del bulletxy[p]
                break


        for q in range(0, len(bulletxy)):
            bulletxy[q][0] = bulletxy[q][0] + 5

        gamepad.fill(WHITE)
        gamepad.blit(background1, (0+xbg1, 0))
        gamepad.blit(background2, (740+xbg2, 0))
        gamepad.blit(aircraft,(x, y))


        if fire != None:
            drawObject(fire, fire_x, fire_y)

        drawObject(bat, bat_x,bat_y)


        for z in range(0, len(bulletxy)):
            drawObject(bullet,bulletxy[z][0],bulletxy[z][1])

        pygame.display.update()
        clock.tick(60)
        if xbg1 == -740:
            xbg1 = 740
        if xbg2 == -1480:
            xbg2 = 0
    pygame.quit()

def initGame():
    global gamepad, clock, aircraft, background1, background2
    global bat, fires, bullet
    fires = []
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    aircraft = pygame.image.load('plane.png')
    pygame.display.set_caption('PyFlying')
    background1 = pygame.image.load('background.png')
    background2 = pygame.image.load('background.png')
    bat = pygame.image.load('bat.png')
    fires.append(pygame.image.load('fireball.png'))
    fires.append(pygame.image.load('fireball2.png'))
    bullet = pygame.image.load('bullet.png')
    clock = pygame.time.Clock()
    runGame()

initGame()