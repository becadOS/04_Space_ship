import pygame
import random

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Enemy_1(Enemy):
    def __init__(self):
        super().__init__()
        self.image = ENEMY_2
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