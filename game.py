import pygame
import sys
import random
from player import Player
from enemy import Enemy
from huevos import Point
from Vidas import Vida
from game_over import game_over
from youWin import youWin

def game(screen):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GRAY = (150, 150, 150)

    clock = pygame.time.Clock()
    runnig = True
    
    all_sprite_list= pygame.sprite.Group()
    
    player= Player(400, 300)
    player.score = 0

    
    all_sprite_list.add(player)
    enemys = pygame.sprite.Group()

    Vidas = pygame.sprite.Group()
    numero_vidas = 3
    for i in  range(numero_vidas):
        desplasar = 50 * i
        vida = Vida(desplasar)
        Vidas.add(vida)
        all_sprite_list.add(vida)

    points = pygame.sprite.Group()
    point = Point()
    point.rect.x = random.randint(0,800)
    point.rect.y = random.randint(0,500)
    points.add(point)
    all_sprite_list.add(point)

    for i in range(2):
        enemy = Enemy()
        enemy.rect.x = random.randint(0,800)
        enemy.rect.y = random.randint(0,500)
        enemys.add(enemy)
        all_sprite_list.add(enemy)

    font_path = "./assets/PressStart2P-Regular.ttf"
    font = pygame.font.Font(font_path, 30)
    background = pygame.image.load('./assets/cesped.jpg').convert()
    hard = 3
    while  runnig :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.chagesspeed(-3,0)
                if event.key == pygame.K_RIGHT:
                    player.chagesspeed(3,0)
                if event.key == pygame.K_UP:
                    player.chagesspeed(0,-3)
                if event.key == pygame.K_DOWN:
                    player.chagesspeed(0,3)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.chagesspeed(3,0)
                if event.key == pygame.K_RIGHT:
                    player.chagesspeed(-3,0)
                if event.key == pygame.K_UP:
                    player.chagesspeed(0,3)
                if event.key == pygame.K_DOWN:
                    player.chagesspeed(0,-3) 
        
        all_sprite_list.update()
        
        if pygame.sprite.spritecollide(player, points, True):
            point.rect.x = random.randint(0,800)
            point.rect.y = random.randint(0,500)
            points.add(point)
            all_sprite_list.add(point)
            player.score +=1
        if player.score >= hard:
            hard += hard
            enemy = Enemy()
            enemy.rect.x = random.randint(0,800)
            enemy.rect.y = random.randint(0,500)
            enemys.add(enemy)
            all_sprite_list.add(enemy)
        if pygame.sprite.spritecollide(player, enemys, True):
            player.score -= 3
            numero_vidas -= 1
            primera_vida = Vidas.sprites()[0]
            Vidas.remove(primera_vida)
            all_sprite_list.remove(primera_vida)
        if player.score == 20:
            runnig = youWin(screen)
            return runnig
        if player.score < 0 or numero_vidas == 0:
            runnig = game_over(screen)
            return runnig
        
        impri_score = font.render('PUNTOS: '+ str(player.score), True, WHITE)
        screen.blit(background,[0,0])
        screen.blit(impri_score,(350, 40))
        all_sprite_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
