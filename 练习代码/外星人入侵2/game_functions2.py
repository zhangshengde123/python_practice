import pygame
import sys
from alien2 import Alien


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x    #alien.rect.x是什么意思?
    aliens.add(alien)
#
#
# def create_fleet(ai_settings, screen, aliens):
#     "创建外星人群"
#     alien = Alien(ai_settings, screen)
#     alien_width = alien.rect.width
#     number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
#     for alien_number in range(number_aliens_x):
#         create_alien(ai_settings, screen, aliens, alien_number)


# def get_number_aliens_x(ai_settings, alien_width):
#     """计算每行可容纳多少个外星人"""
#     available_space_x = ai_settings.screen_width - 2 * alien_width
#     number_aliens_x = int(available_space_x / (2 * alien_width))
#     return number_aliens_x
# def create_alien(ai_settings, screen, aliens, alien_number):
#     """创建一个外星人并将其放在当前行"""
#     alien = Alien(ai_settings, screen)
#     alien_width = alien.rect.width
#     alien.x = alien_width + 2 * alien_width * alien_number
#     alien.rect.x = alien.x
#     aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算每行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)





    # def create_fleet(ai_settings, screen, aliens):
#     "创建外星人群"
#     alien = Alien(ai_settings, screen)
#     alien_width = alien.rect.width
#     available_space_x = ai_settings.screen_width - 2 * alien_width
#     number_aliens_x = int(available_space_x/(2*alien_width))
#     for alien_number in range(number_aliens_x):
#         alien = Alien(ai_settings, screen)
#         alien.x = alien_width + 2 * alien_width * alien_number
#         alien.rect_x = alien.x
#         aliens.add(alien)
#


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    #上下移动控制
    elif event.key == pygame.K_UP:
        ship.moving_upward = True
    elif event.key == pygame.K_DOWN:
        ship.moving_downward = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    # 上下移动控制
    elif event.key == pygame.K_UP:
        ship.moving_upward = False
    elif event.key == pygame.K_DOWN:
        ship.moving_downward = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


"""
重构前的代码
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

"""


def update_screen(ai_settings, screen, ship, bullets, aliens):

    screen.fill(ai_settings.bg_color)  # 填充背景颜色
    ship.blit_me()
    bullets.draw_bullet()
    #alien.blit_me()
    aliens.draw(screen)
    pygame.display.flip()