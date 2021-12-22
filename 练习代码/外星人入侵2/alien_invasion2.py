import pygame
import sys
from settings2 import Setting
from ship2 import Ship
from alien2 import Alien
import game_functions2 as gf
from pygame.sprite import Group



def game_run():

    pygame.init()
    ai_settings = Setting()
    # bg_color = (255, 0, 0)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵2")
    ship = Ship(ai_settings, screen)
    #alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)

    while True:
        # screen.fill(ai_settings.bg_color)                #填充背景颜色
        # ship.blit_me()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #
        pygame.display.flip()
        gf.check_events(ship)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)



game_run()
