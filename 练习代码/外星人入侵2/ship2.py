import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self,ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #self.screen_rect = screen.get_rect()

        """"""
        self.image = pygame.image.load('image2/ship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """"""

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        #
        self.center = float(self.rect.centerx)
        self.y = float(self.rect.y)

        """设置飞船移动标志"""
        self.moving_right = False
        self.moving_left = False
        self.moving_upward = False
        self.moving_downward = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_limit

        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.speed_limit

         # gfh2
        elif self.moving_upward:
            self.y -= self.ai_settings.speed_limit
        elif self.moving_downward:
            self.y += self.ai_settings.speed_limit

        self.rect.centerx = self.center
        self.rect.y = self.y

    def blit_me(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def print_me(self):
        print(self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx



