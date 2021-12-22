import pygame
from pygame.sprite import Sprite


# class Alien(Sprite):
#     def __init__(self, ai_settings, screen):
#         super(Alien, self).__init__()
#         self.ai_setting = ai_settings
#         self.screen = screen
#
#         self.image = pygame.image.load('images/alien.bmp')
#         self.rect = self.image.get_rect()
#         self.screen_rect = screen.get_rect()
#
#         self.rect.x = self.screen_rect.width
#         self.rect.y = self.screen_rect.height
#
#         self.x = float(self.rect.x)
#
#         def blit_me(self):
#
#             self.screen.blit(self.image, self.rect)
#
#         def update(self):
#             self.x = (self.ai_settings.alien_speed_factor * self.ai_settings.fleet.direction)
#             self.rect.x = self.x
#
#         def check_edges(self):
#             screen_rect = self.screen.get_rect()
#             if self.rect.right >= screen_rect.right:
#                 return True
#             elif self.rect.left <= 0:
#                 return True


class Alien(Sprite):
    """ 表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """ 初始化外星人并设置其起始地址"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blit_me(self):
        """ 在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 向左或向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ 如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True








