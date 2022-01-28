class GameStats():
    """跟踪游戏的统计数据"""
    def __init__(self, ai_settings):
        """初始化统计信息"""

        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        #最高得分
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        # 等级
        self.level = 1