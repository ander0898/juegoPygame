import pygame
from menu import show_menu 
from game import game
screen_Width = 900
screen_Height = 600
def main():
    pygame.init()
    screen = pygame.display.set_mode([screen_Width, screen_Height])
    pygame.display.set_caption('Mi juego')

    while True:
        option = show_menu(screen)
        if option == 'start':
            res = game(screen)
            if not res:
                main()
        elif option == 'exit':
            break
    pygame.quit()

if __name__ == "__main__":
    main()