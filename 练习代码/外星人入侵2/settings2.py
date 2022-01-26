class Setting():

    def __init__(self):
        self.bg_color = (230, 230, 230)
        self.screen_width = 1200
        self.screen_height = 800
        self.speed_limit = 1.5


        #外星人偏移
        self.fleet_edge = 2
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1
        self.bullet_allowed = 5

        #飞船设置
        self.ship_limit = 3
        self.ship_speed_factor = 1.5