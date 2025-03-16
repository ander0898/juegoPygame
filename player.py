import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.original_image = pygame.image.load('./assets/snake.png')
        self.image = self.original_image
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speedX = 0
        self.speedY = 0
        self.last_direction = "left" 
        self.score = 0
    def chagesspeed(self,x,y):
        self.speedX +=x
        self.speedY +=y
        
    def update(self):
        current_center = self.rect.center

        # Determinar dirección basada en la velocidad
        if self.speedX > 0:
            new_direction = "right"
        elif self.speedX < 0:
            new_direction = "left"
        elif self.speedY < 0:
            new_direction = "up"
        elif self.speedY > 0:
            new_direction = "down"
        else:
            new_direction = self.last_direction  # Sin movimiento, mantener dirección

        # Cambiar imagen solo si la dirección cambió
        if new_direction != self.last_direction:
            if new_direction == "right":
                self.image = pygame.transform.flip(self.original_image, True, False)
            elif new_direction == "left":
                self.image = self.original_image
            elif new_direction == "up":
                self.image = pygame.transform.rotate(self.original_image, -90)  
            elif new_direction == "down":
                self.image = pygame.transform.rotate(self.original_image, 90)  
            
            self.image.set_colorkey([0, 0, 0])  
            self.last_direction = new_direction

            self.rect = self.image.get_rect(center=current_center)

        if self.rect.x > 800 :
            self.rect.x = 800
        elif self.rect.x < 0:
            self.rect.x = 0
        else :
            self.rect.x += self.speedX
        
        if self.rect.y > 490 :
            self.rect.y = 490
        elif self.rect.y < 0:
            self.rect.y = 0
        else :
            self.rect.y += self.speedY
    