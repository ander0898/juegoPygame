import pygame

def  show_menu(screen):
    black = (0,0,0)
    white = (255,255,255)
    font_path = "./assets/PressStart2P-Regular.ttf"
    font = pygame.font.Font(font_path, 30)
    clock = pygame.time.Clock()
    background = pygame.image.load('./assets/menu.png').convert()
    while True:
        screen.blit(background,[0,-100])
        title = font.render('serpiente vs gallinas ', True, black)
        start  = font.render('1. Inciar Juego', True, black)
        exit = font.render('2. Salir', True, black)

        screen.blit(title, (300, 250))
        screen.blit(start, (300, 300))
        screen.blit(exit, (300,350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 'start'
                if event.key == pygame.K_2:
                    return'exit'
        clock.tick(15)