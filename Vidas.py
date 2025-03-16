import pygame

class Vida(pygame.sprite.Sprite):
    def __init__(self,x):
        super().__init__()
        self.image = pygame.image.load('./assets/corazon.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (700+x, 50)
