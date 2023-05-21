import pygame
import random


class Shield(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.iamge = pygame.image.load("PNG\\Effects\\shield1.png").convert.aplha()
        self.rect = self.image.get_rect()
        self.rect.center = self.player.rect.center
        self.last_update = pygame.time.get_ticks()
        self.radius = self.rect.width // 2

        def update(self):
            self.rect.center = self.player.center
            now = pygame.time.get_ticks()
            if now - self.last_update > 5000:
                self.last_update = now
                self.kill()
