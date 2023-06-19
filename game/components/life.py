import pygame

from game.utils.constants import ICON

class Life:
    def __init__(self, life = 1):
        self.life = life
        
    def update(self, subject):
        self.life -= 1
        if subject.life.life <= 0:
            subject.is_alive = False
        else:
            subject.is_alive = True
            
    def increases_life(self,lifes):
        self.life += lifes
            
    def draw (self, screen):
        self.image = ICON
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.rect = self.image.get_rect()
        for counter in range(self.life):
            self.rect.center = ((1070 - (counter*35)), 580)
            screen.blit(self.image, (self.rect.x , self.rect.y))