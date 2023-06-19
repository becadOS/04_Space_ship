import pygame
import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_1 import Enemy_1
from game.components.enemies.enemy_2 import Enemy_2
from game.components.enemies.enemy_3 import Enemy_3


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.when_appears_enemy = random.randint(500,1000)
        self.when_appears_enemy_2 = random.randint(3000,5000)
        self.when_appears_boss = random.randint(60*1000,70*1000)
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        
        
    def add_enemy(self):
        current_time = pygame.time.get_ticks()
        if current_time >= self.when_appears_enemy:
            self.when_appears_enemy += random.randint(1000,2000)
            self.enemies.append(Enemy())
        if current_time >= self.when_appears_enemy_2:
            self.when_appears_enemy_2 += random.randint(3000,5000)
            self.enemies.append(Enemy_2())
            self.enemies.append(Enemy_3())
            
            
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def reset(self):
        self.enemies = []