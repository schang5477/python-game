import pygame

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370



def runGame():
    global gamepad, clock, aircraft, background1, background2
    global greenpole1, greenpole2

    crashed = False
    x = pad_width * 0.05
    y = pad_height * 0.8
    x1 = 0
    x2 = 0
    y_change = 0
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_change = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x1 -= 5
        x2 -= 5

        y += y_change

        y+=2

        gamepad.fill(WHITE)
        gamepad.blit(background1, (0+x1, 0))
        gamepad.blit(background2, (740+x2, 0))
        gamepad.blit(aircraft,(x, y))
        pygame.display.update()
        clock.tick(60)
        if x1 == -740:
            x1 = 740
        if x2 == -1480:
            x2 = 0
    pygame.quit()

def initGame():
    global gamepad, clock, aircraft, background1, background2
    global greenpole1, greenpole2

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    aircraft = pygame.image.load('plane.png')
    pygame.display.set_caption('PyFlying')
    background1 = pygame.image.load('background.png')
    background2 = pygame.image.load('background.png')
    greenpole1 = pygame.image.load('flappy-bird-pipes-png-2.png')
    greenpole2 = pygame.image.load('flappy-bird-pipes-png-2.png')

    clock = pygame.time.Clock()
    runGame()

initGame()