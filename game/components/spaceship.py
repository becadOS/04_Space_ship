import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_TYPE , SHIELD_TYPE
from game.components.bullets.bullet import Bullet
from game.components.life import Life

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2)
    Y_POS = SCREEN_HEIGHT // 2
    SHOOTING_TIME = 1
    
    def __init__ (self):
        self.size = 25
        self.spacechip_width = SCREEN_WIDTH // self.size
        self.spacechip_height = self.spacechip_width * 1.5
        self.image = pygame.transform.scale(SPACESHIP, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        
        self.life = Life(3)
        self.is_alive = True
        
        self.type = 'player'
        self.shooting_time = 0
        
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE
        
    
    
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
        self.shooting_time += 1
        self.collision_enemy(game)
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
        self.center = self.rect.center
            
    def shoot(self, bullet_manager):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            
    def collision_enemy (self,game):
        for enemy in game.enemy_manager.enemies:
            if enemy.rect.colliderect(game.player) and self.power_up_type != SHIELD_TYPE:
                game.enemy_manager.enemies.remove(enemy)
                game.score.update()
                game.player.life.update(game.player)
                if not(game.player.is_alive):
                    game.death_count.update()
                    game.player.is_alive = False
                    pygame.time.delay(1000)

            elif enemy.rect.colliderect(game.player) and self.power_up_type == SHIELD_TYPE:
                game.enemy_manager.enemies.remove(enemy)
                game.score.update()
            
    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = Life(3)
        self.is_alive = True
        
    def set_image(self, size = (40,60), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, (size))
    
            
    def draw (self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))