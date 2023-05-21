import pygame 
from randint import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("playerShip2_orange.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speedx = 10
        self.gun_bonus = False
        self.gun_bonus_timer = pygame.time.get_triks()

        if keys[pygame.K_LEFT]
        x -= 5
        if keys[pygame.K_RIGHT]
        x += 5



        now= pygame.time.get_ticks()
        if self.gun_bonus and now - self.gun_bonus_timer > 5000:
            self.gun_bonus = False
