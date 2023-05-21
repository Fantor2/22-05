from settings import *
import pygame


class Meteor(pygame.sprite.Sprite):

    def __init__(self,screen,x,y):
        self.screen = screen 
        pygame.sprite.Sprite.__init(self)
        self.image = pygame.image.load(METEOR_FILE_NAME).covert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = 2
        if self.rect.width >80:
            self.damage = 50
        elif self.rect.width <80 and self.rect.width > 40:
            self.damage = 30  
        elif self.rect.width <35 and self.rect.width > 5:
            self.damage = 5
        if random.randint(100) > 90:
            bonus = Bonus(bonus_image_dict, hit_rect.center)
            bonuses.add(bonus)
            all_sprites.add(bonus)
    def update(self):
        self.rect.y +=self.speedy
        def draw (self):
            self.screen_blit(self.image.self.rect)
        
