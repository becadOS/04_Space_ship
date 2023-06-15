import pygame
import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_1 import Enemy_1
from game.components.enemies.enemy_2 import Enemy_2
from game.components.enemies.enemy_3 import Enemy_3


class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        
        
    def add_enemy(self):
        if len(self.enemies)<4:
            self.enemies.append(Enemy())
            self.enemies.append(Enemy_1())
            self.enemies.append(Enemy_2())
            self.enemies.append(Enemy_3())
            
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)