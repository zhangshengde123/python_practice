import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()

        #
        self.ai_settings = ai_settings
        self.screen = screen
        #
        self.image = pygame.image.load('image2/alien2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #指定位置
        self.rect_x = self.rect.width
        self.rect_y = self.rect.height

        self.x = float(self.rect_x)



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

    def blit_me(self):
        self.screen.blit(self.image, self.rect)


