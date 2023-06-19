import pygame
from game.utils.constants import SHIELD_TYPE, SHOOT_SPACESHIP, SHOOT_ENEMY


class BulletManager:
    def __init__(self) :
        self.enemy_bullets = []
        self.player_bullets = []
        
        
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            
            if bullet.rect.colliderect(game.player) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE: 
                    game.player.life.update(game.player)
                    if not(game.player.is_alive):
                        game.death_count.update()
                        game.player.is_alive = False
                        pygame.time.delay(1000)
                break
            
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy) and bullet.owner == 'player':
                    self.player_bullets.remove(bullet)
                    enemy.life.update(enemy)
                    if not(enemy.is_alive):
                        game.enemy_manager.enemies.remove(enemy)
                    game.score.update()
                    break

    
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == 'enemy':
            self.enemy_bullets.append(bullet)
            SHOOT_ENEMY.play()
        if bullet.owner == 'player' and len(self.player_bullets) < 5:
            self.player_bullets.append(bullet)
            SHOOT_SPACESHIP.play()
        
    def reset(self):
        self.enemy_bullets = []
        self.player_bullets = []
            