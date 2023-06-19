import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.life_power import LifePower
from game.components.power_ups.bullet import BulletPower
from game.utils.constants import LIFE_TYPE, SPACESHIP, SHIELD_TYPE,BULLET_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.power_ups_active = []
        self.is_shield = False
        self.when_appears_shield = random.randint(5000,10000)
        self.when_appears_life = random.randint(10000,20000)
        self.is_bullet = False
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
            power_up = BulletPower()
            self.when_appears_bullet += random.randint(30000,40000)
            self.power_ups.append(power_up)
            
    def active_power(self, power):
        self.power_ups_active.append(power)
        
    def desactivate_power(self, power):
        if power.type == SHIELD_TYPE:
            self.is_shield = False
        if power.type == BULLET_TYPE:
            self.is_bullet = False
        self.power_ups_active.remove(power)
        
    def update (self,game):
        current_time = pygame.time.get_ticks()
        
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                self.power_ups_active.append(power_up)
                power_up.time_up = power_up.start_time + (self.duration * 1000)
                if not(power_up.spaceship_image == SPACESHIP):
                    game.player.set_image((65,75),power_up.spaceship_image)
                self.power_ups.remove(power_up)
                if power_up.type == LIFE_TYPE:
                    game.player.life.increases_life(2)
        
        for power_up_active in self.power_ups_active:
            if power_up_active.type == SHIELD_TYPE:
                self.is_shield = True
            if power_up_active.type == BULLET_TYPE:
                self.is_bullet = True
                
    def draw (self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset (self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000,10000)