import pygame
import sys
from settings2 import Setting
from ship2 import Ship
from alien2 import Alien
from button2 import Button
from scoreboard2 import Scoreboard
from  game_stats2 import GameStats
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
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    sb = Scoreboard(ai_settings, screen, stats)


    while True:
        # screen.fill(ai_settings.bg_color)                #填充背景颜色
        # ship.blit_me()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #
        pygame.display.flip()
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            #  删除 消失的子弹
            gf.bullet_update(ai_settings, screen, stats, ship, aliens, bullets, sb)
            #print(bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button, sb)




game_run()
