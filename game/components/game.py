import pygame

from game.utils.constants import BG, ICON , SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, LIFE_TYPE, SHIELD_TYPE,BULLET_TYPE

from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.counter import Counter
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__ (self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
        self.clock = pygame.time.Clock()
        
        self.running = False
        self.playing = False
        self.game_speed = 10
        
        #self.score_max = 0
        #self.score = 0
        #self.death_count = 0
        
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.menu = Menu(self.screen)
        
        
    def execute(self):
        self.running = True
        while self.running:
            if not(self.playing):
                self.show_menu()
                pygame.mixer.music.stop()
        pygame.display.quit()
        pygame.quit()
                

    def run(self):
        self.reset()
        pygame.mixer.music.load("game/assets/Sound/Fondo.mp3")
        pygame.mixer.music.play(4)
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset(self):
        self.score.reset()
        self.player.reset()
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.power_up_manager.reset()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
    
    def update(self):
        if not(self.player.is_alive): self.playing = False
        user_input = pygame.key.get_pressed()
        self.player.update(user_input,self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        
    
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill( (255, 255, 255))
        
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.score.draw(self.screen)
        self.player.life.draw(self.screen)
        
        pygame.display.update()
        pygame.display.flip()
        
        
    def draw_power_up_time(self):
        for power_up in self.power_up_manager.power_ups_active:
            time_to_show = round((power_up.time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0:
                if  power_up.type == SHIELD_TYPE :
                    self.menu.draw(self.screen, f'{power_up.type.capitalize()} is enabled for {time_to_show} in seconds', 500,50, (255,255,255))
            else:
                self.power_up_manager.desactivate_power(power_up)
                self.player.set_image()
                if power_up.type == SHIELD_TYPE:
                    self.power_up_manager.is_shield = False
                if power_up.type == BULLET_TYPE:
                    self.power_up_manager.is_bullet = False
    
    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg = self.y_pos_bg + self.game_speed    
        
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        haft_screen_height = SCREEN_HEIGHT // 2
        haft_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count.count == 0 :
            self.menu.draw(self.screen, 'Press any key to start')
        else:
            self.update_highest_score()
            
            self.menu.draw(self.screen, 'Game over, Press any key to restart...')
            self.menu.draw(self.screen, f'Your score: {self.score.count}', haft_screen_width, 350,)
            self.menu.draw(self.screen, f'Your highest score: {self.highest_score.count}', haft_screen_width, 400,)
            self.menu.draw(self.screen, f'Total death: : {self.death_count.count}', haft_screen_width, 450,)
            
        icon = pygame.transform.scale(ICON, (80,120))
        self.screen.blit(icon,(haft_screen_width - 50, haft_screen_height - 150))
        self.menu.update(self)
    
    
    def update_highest_score(self):
        if self.highest_score.count < self.score.count:
            self.highest_score.set_count(self.score.count)
        
        

        