import pygame,sys
def  youWin(screen):
    black = (0,0,0)
    white = (255,255,255)
    font_path = "./assets/PressStart2P-Regular.ttf"
    font = pygame.font.Font(font_path, 30)
    clock = pygame.time.Clock()
    background = pygame.image.load('./assets/win.png').convert()
    salir = False
    while not salir:
        screen.blit(background,[0,-50])
        font = pygame.font.SysFont('serif', 25)
        text = font.render('YOU WIN, Click to Continue', True, black)
        center_x = (900 //2)-(text.get_width() // 2)
        center_y = (600 //2)-(text.get_height() // 2)
        screen.blit(text, [center_x, center_y])

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                salir = True
                return False
        clock.tick(15)