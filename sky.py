import pygame
from settings import *

class Sky(pygame.sprite.Sprite):
    def __init__(self,filename,screen, x, y):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
    def update(self):
        self.rect.y += 2
        if self.rect >= 1000:
            self.rect.y = -1000
    def draw(self):
        self.screen.blit(self.image,self.rect)
