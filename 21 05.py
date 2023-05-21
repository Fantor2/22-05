import pygame
import sys
from sky import Sky
from settings import *
import random
from meteor import Meteor
from bullet import Bullet
pygame.init()
screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
sky = Sky("sky.png",screen , SCREEN_WIDTH , SCREEN_HEIGHT) 

meteors = pygame.sprite.Group()
meteors.add(meteor)
all_sprites.add(meteor)

bullets_hits_meteors = pygame.sprite.groupcollide(meteors, bullets, True , True)
for hit in bullets_hits_meteors:
    if hit.radius >= 35:
        score +=5
    elif hit.radius < 35 and hit.radius >= 17:
        score +=10
    elif hit.radius <17 and hit.radius >= 11:
        score +=20
    else:
        score +=40

if random.randint(0,100) < 10:
    bonus = Bonus
    bonuses.add(bonus)
    all_sprites.add(bonus)



player_hits_bonuses = pygame.sprite.spritecollide(player, bonuses, True, pygame.sprite.collide_circle)
for hit in player_hits_bonuses:
    if hit.type == 'hp':
        player.hp += random.randint(20, 50)
        if player.hp > 100:
            player.hp = 100
        elif hit.type == 'gun':
            player.gun.bonus = True
            player.gun_bonus_timer = pygame.time.get_ticks()
        elif hit.type == 'shield':
            shield = shield



while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



                if player.gun_bonus:
                    bullet = Bullet(player.rect.centerx, player.rect.midright)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
sky1 = Sky('sky.png',screen,(SCREEN_WIDTH - 200) // 2,0)
sky2 = Sky('sky.png',screen,(SCREEN_WIDTH - 200) // 2, - SCREEN_HEIGHT)

sky.update()
screen_fill((0,0,0))
pygame.display.update()
