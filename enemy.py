import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load('./assets/galloenojado.png')
        self.image = self.original_image
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.speedX = 3
        self.speedY = 3
        self.last_direction = "left" 
    # def chagesspeed(self,x,y):
    #     self.speedX +=x
    #     self.speedY +=y
        
    def update(self):

        # Determinar dirección basada en la velocidad
        if self.speedX > 0:
            new_direction = "right"
        elif self.speedX < 0:
            new_direction = "left"
        else:
            new_direction = self.last_direction  # Sin movimiento, mantener dirección

        # Cambiar imagen solo si la dirección cambió
        if new_direction != self.last_direction:
            if new_direction == "right":
                self.image = pygame.transform.flip(self.original_image, True, False)
            elif new_direction == "left":
                self.image = self.original_image


        if self.rect.x > 800 or self.rect.x < 0 :
            self.speedX *=-1
        
        if self.rect.y > 500 or self.rect.y < 0 :
            self.speedY *=-1

        self.rect.x += self.speedX
        self.rect.y += self.speedY