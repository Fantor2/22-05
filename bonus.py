import pygame


class Bonus(pygame.sprite.Sprite):
    def __init__(self, image_dict, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['hp', 'gun', 'shield'])
        self.image = image_dict[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get.rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rec.top > SCREEN_HEIGHT:
            self.kill()
