import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(Sprite):
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    MOV_X = {0: 'left', 1: 'right'}


    
    def __init__(self):
        super().__init__()
        self.image = ENEMY_1
        self.size = random.randint(15,30)
        self.enemy_width = SCREEN_WIDTH // self.size
        self.enemy_height = self.enemy_width * 1.5
        self.image = pygame.transform.scale(self.image, (self.enemy_width, self.enemy_height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1,20)*50
        self.rect.y = self.Y_POS
        
        self.SPEED_X = self.SPEED_X
        self.SPEED_Y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(30,100)
        self.index = 0
        self.shooting_time = random.randint(30, 50)
        
        
        
    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - 40): 
            self.movement_x = 'left'
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            
        if self.index >= self.move_x_for:
            self.index = 0
    
    def update(self, ships):
        self.rect.y += self.SPEED_Y
        
        if self.movement_x == 'left':
            self.rect.x -= self.SPEED_X
            self.change_movement_x()
        else:
            self.rect.x += self.SPEED_X
            self.change_movement_x()
        if self.rect.y >= SCREEN_HEIGHT:
            self.move_x_for = random.randint(30,100)
            ships.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        