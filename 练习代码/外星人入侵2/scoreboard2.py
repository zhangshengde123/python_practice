import pygame.font
from pygame.sprite import Group
from ship2 import Ship


class Scoreboard():
    """得分板"""
    def __init__(self, ai_settings, screen, stats):

        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.width = 50
        self.height = 30
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将score渲染为图片，并展示在右上角"""
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        # score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prep_high_score(self):
        """将high_score最高分渲染为图片，并使得其在屏幕顶部内居中"""
        round_high_score = round(self.stats.high_score, -1)
        print(round_high_score)
        high_score_str = "{:,}".format(round_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_image_rect = self.score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.score_image_rect.top

    def prep_level(self):
        """将level飞船等级渲染为图片，并展示在分数下方"""
        #level = str(self.stats.level)
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom + 10


    def prep_ships(self):
        """在屏幕左上角显示还剩多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):

        self.screen.blit(self.score_image, self.score_image_rect)

        self.screen.blit(self.high_score_image, self.high_score_image_rect)

        self.screen.blit(self.level_image, self.level_image_rect)

        self.ships.draw(self.screen)
