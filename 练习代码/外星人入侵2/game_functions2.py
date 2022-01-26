import pygame
import sys
from alien2 import Alien
from bullet2 import Bullet
from time import sleep


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x    #alien.rect.x是什么意思?

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
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


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算每行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)  #计算屏幕最多展示多少行外星人
    # 创建多行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳的外星人行数"""
    avaliable_space_y = ai_settings.screen_height - ship_height - 3 * alien_height
    number_rows = int(avaliable_space_y/(2 * alien_height))
    return number_rows




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

def bullet_update(ai_settings, screen, ship, aliens, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹击中了外星人
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):

    # 检查是否有子弹击中了外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:  # 删除现有的子弹并创建新的一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)





def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    #上下移动控制
    elif event.key == pygame.K_UP:
        ship.moving_upward = True
    elif event.key == pygame.K_DOWN:
        ship.moving_downward = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

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


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
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
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blit_me()

    #alien.blit_me()
    aliens.draw(screen)
    pygame.display.flip()



def change_fleet_direction(ai_settings, aliens):
    """ 将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """ 有外星人到达边缘时采取向右相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_buttom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #检查外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_buttom(ai_settings, stats, screen, ship, aliens, bullets)





