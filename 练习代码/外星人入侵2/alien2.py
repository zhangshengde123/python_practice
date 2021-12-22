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



    def blit_me(self):
        self.screen.blit(self.image, self.rect)




