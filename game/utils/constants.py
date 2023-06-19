import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
BULLET_POWER = pygame.image.load(os.path.join(IMG_DIR, 'Other/bullet_power.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
LIFE = pygame.image.load(os.path.join(IMG_DIR, 'Other/Life.png'))

DEFAULT_TYPE = 'default'
SHIELD_TYPE = 'shield'
LIFE_TYPE = 'life'
BULLET_TYPE = 'bullet'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))
OVNI = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ovni.png"))

pygame.mixer.init()
SHOOT_SPACESHIP = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/Shoot_spaceship.mp3"))
SHOOT_ENEMY = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/Shoot_enemy.mp3"))

FONT_STYLE = 'freesansbold.ttf'
