import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.life_power import LifePower
from game.components.power_ups.bullet import BulletPower
from game.utils.constants import LIFE_TYPE, SPACESHIP


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.power_ups_active = []
        self.when_appears_shield = random.randint(5000,10000)
        self.when_appears_life = random.randint(10000,20000)
        self.when_appears_bullet = random.randint(500,1000)
        self.duration = random.randint(3,5)
        
    def generate_power_up (self):
        current_time = pygame.time.get_ticks()
        if current_time >= self.when_appears_shield:
            power_up = Shield()
            self.when_appears_shield += random.randint(5000,10000)
            self.power_ups.append(power_up)
        if  current_time >= self.when_appears_life:
            power_up = LifePower()
            self.when_appears_life += random.randint(10000,20000)
            self.power_ups.append(power_up)
        if  current_time >= self.when_appears_bullet:
            print("bullet")
            power_up = BulletPower()
            self.when_appears_bullet += random.randint(500,1000)
            self.power_ups.append(power_up)
            
    def active_power(self, power):
        self.power_ups_active.append(power)
        
    def desactivate_power(self, power):
        self.power_ups_active.remove(power)
        
    def update (self,game):
        current_time = pygame.time.get_ticks()
        
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_up_type = power_up.type
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                if not(power_up.spaceship_image == SPACESHIP):
                    game.player.set_image((65,75),power_up.spaceship_image)
                self.power_ups.remove(power_up)
                if game.player.power_up_type == LIFE_TYPE:
                    game.player.life.increases_life(2)
                
                
    def draw (self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset (self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000,10000)