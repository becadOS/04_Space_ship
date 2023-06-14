import pygame
import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_1 import Enemy_1
from game.components.enemies.enemy_2 import Enemy_2
from game.components.enemies.enemy_3 import Enemy_3


class EnemyManager:
    ENEMIE = [Enemy(), Enemy_1(), Enemy_2(), Enemy_3()]
    def __init__(self):
        self.enemies = pygame.sprite.Group()
    
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)
        
        
    def add_enemy(self):
        if len(self.enemies)<5:
            ran = random.randint(0, 3)
            self.enemies.add(self.ENEMIE[ran])
            
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)