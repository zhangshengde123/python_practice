import pygame
from settings import Settings
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from all_music import bg_music

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(("Alien Invasion"))
    #
    #pygame.mixer.init()

    #
    play_button = Button(ai_settings, screen, "Play")

    #
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #
    #bg_music()
    """开始游戏的主循环"""
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            #gf.play_bg_music()
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings,screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()



