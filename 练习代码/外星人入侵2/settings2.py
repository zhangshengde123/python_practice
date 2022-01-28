class Setting():

    def __init__(self):
        #屏幕设置
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
        self.bullet_width = 300
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1
        self.bullet_allowed = 5

        #飞船设置
        self.ship_limit = 3
        self.ship_speed_factor = 1.5

        #以什么样的速度加快游戏节奏
        self.speed_scale = 1.1
        self.inittialize_dynamic_settings()

        self.score_scale = 1.5

    def inittialize_dynamic_settings(self):
        """游戏初始设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50


    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points *= self.score_scale
        print(self.alien_points)


