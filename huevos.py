import pygame

class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/huevo.png')
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()