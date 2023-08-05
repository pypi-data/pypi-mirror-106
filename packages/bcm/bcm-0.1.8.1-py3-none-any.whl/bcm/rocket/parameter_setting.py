import pygame
import os

# 文件目录
USER_DIR = os.getcwd()
SYS_DIR = os.path.split(os.path.realpath(__file__))[0]
SYS_RESOURCES_DIR = SYS_DIR + os.sep + "rkimg"


class GameSetting:
    # 要不要判断空格是否按下
    judge_key = False
    # 按键有效次数 = 设置的范围次数, 第一次起飞不计数
    key_valid_count = 1

    def __init__(self):
        # 是否绘制火箭
        self.is_draw_rocket = False
        # 窗口设置
        self.screen_width = 400
        self.screen_height = 650
        self.screen_title = "火箭发射"
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # 窗体背景
        self._bg_name = "bg.png"
        # 火箭颜色
        self._rk_color = "white"

        # 游戏状态
        self.game_status = 0

        # 设定游戏状态
        self.GAME_INIT = 0
        self.GAME_WIN = 1
        self.GAME_LOSE = 2

        # 火箭高度
        self.height = 0

        # 火箭各级对应高度范围
        self.range0 = 300  # 逃逸塔脱落对应的高度范围(虚拟数据)
        self.range0_1 = 500

        self.range1 = 700  # 助推器脱落（同上）
        self.range1_1 = 1000

        self.range2 = 1800  # 一级火箭脱落（同上）
        self.range2_1 = 2200

        self.range3 = 3000  # 整流罩（同上）
        self.range3_1 = 3400

        self.range4 = 4200  # 二级火箭脱落（同上）
        self.range4_1 = 5800

        # 火箭的初速度和加速度
        self.MOVE_SPEED = 3
        self.ACCELERATE_SPEED = 3

        # 蓝色火焰计时
        self.timer = 0

        # 空格按下次数
        self.press_count = 0

        # 素材路径
        self.bg_top_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._bg_name}{os.sep}top_image.png"
        self.bg_bottom_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._bg_name}{os.sep}bottom_image.png"

        self.height_frame_path = f"{SYS_RESOURCES_DIR}{os.sep}height_bottom.png"

        # 火箭状态与对应的状态提示图片路径
        self.rk_state = ["launching", "et", "booster", "first", "mask", "sa"]
        self.rk_state_path = []
        for i in range(6):
            rk_temp_path = f"{SYS_RESOURCES_DIR}{os.sep}rk_state{os.sep}state{i}.png"
            self.rk_state_path.append(rk_temp_path)
        self.result_win_path = f"{SYS_RESOURCES_DIR}{os.sep}game_state{os.sep}win.png"
        self.result_lose_path = f"{SYS_RESOURCES_DIR}{os.sep}game_state{os.sep}lose.png"

        self.space_vehicle_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}space_vehicle.png"
        self.tower_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}tower.png"
        self.mask1_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}mask1.png"
        self.mask2_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}mask2.png"
        self.second_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}second.png"
        self.first_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}first_image.png"
        self.push1_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}push1.png"
        self.push2_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}push2.png"
        self.push3_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}push3.png"
        self.push4_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}push2.png"
        self.rocket_list = [self.space_vehicle_path, self.tower_path, self.mask1_path, self.mask2_path,
                            self.second_path, self.first_path, self.push1_path, self.push2_path, self.push3_path,
                            self.push4_path]

        # 火焰路径
        self.fire_path = f"{SYS_RESOURCES_DIR}{os.sep}fire"
        # 烟雾路径
        self.smoke_path = f"{SYS_RESOURCES_DIR}{os.sep}smoke"

        # 音乐素材路径
        self.bg_music_path = f"{SYS_RESOURCES_DIR}{os.sep}music{os.sep}music.mp3"
        self.failure_music_path = f"{SYS_RESOURCES_DIR}{os.sep}music{os.sep}failure.wav"
        self.accelerate_music_path = f"{SYS_RESOURCES_DIR}{os.sep}music{os.sep}accelerate.wav"

        # 各个零件掉落的初始速度
        self.fail_speed = 1

    @property
    def bg_name(self):
        return self._bg_name

    @bg_name.setter
    def bg_name(self, value):
        self._bg_name = value
        # 素材路径
        self.bg_top_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._bg_name}{os.sep}top_image.png"
        self.bg_bottom_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._bg_name}{os.sep}bottom_image.png"

    @property
    def rk_color(self):
        return self._bg_name

    @rk_color.setter
    def rk_color(self, value):
        self._rk_color = value
        # 素材路径
        self.space_vehicle_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}space_vehicle.png"
        self.tower_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}tower.png"
        self.mask1_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}mask1.png"
        self.mask2_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}mask2.png"
        self.second_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}second.png"
        self.first_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}first_image.png"
        self.push1_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}push1.png"
        self.push2_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}push2.png"
        self.push3_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}push3.png"
        self.push4_path = f"{SYS_RESOURCES_DIR}{os.sep}{self._rk_color}{os.sep}push2.png"
        self.rocket_list = [self.space_vehicle_path, self.tower_path, self.mask1_path, self.mask2_path,
                            self.second_path, self.first_path, self.push1_path, self.push2_path, self.push3_path,
                            self.push4_path]
