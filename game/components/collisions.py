import pygame

class Collision:
    def collision_enemies(self, spaceship, enemy_list):
        self.spaceship = spaceship
        self.enemy_list = enemy_list
        self.hits = pygame.sprite.spritecollide(spaceship, enemy_list, True)
        