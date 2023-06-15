import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2)
    Y_POS = SCREEN_HEIGHT // 2
    
    def __init__ (self):
        self.size = 25
        self.spacechip_width = SCREEN_WIDTH // self.size
        self.spacechip_height = self.spacechip_width * 1.5
        self.image = pygame.transform.scale(SPACESHIP, (self.spacechip_width, self.spacechip_height))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.shooting_time = random.randint(40, 60)
    
    
    def move_left (self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH - self.rect.width
    def move_right (self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0
    def move_up (self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10 
    def move_down (self):
        if self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y += 10  
            
    def update (self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
            
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(20, 50)
            
    def draw (self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))