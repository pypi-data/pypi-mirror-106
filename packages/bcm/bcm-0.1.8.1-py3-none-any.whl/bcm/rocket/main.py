from pygame.locals import *  # 从pygame本地导入所有函数或者对象
import pygame
from .interface_element import Background, HintFrame, HeightFrame, ResultImg, Smoke
from .parameter_setting import GameSetting
from .rocket import Rocket, Fire


# 游戏主程序
class GameWindow:
    def __init__(self):
        pygame.init()
        # 导入设置文件
        self.st = GameSetting()
        self.screen = self.st.screen
        pygame.display.set_caption(self.st.screen_title)
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        # 背景音乐加载
        pygame.mixer_music.load(self.st.bg_music_path)
        pygame.mixer.music.set_volume(0.07)
        pygame.mixer.music.play(-1)
        # 音效设置
        self.accelerate_music = pygame.mixer.Sound(self.st.accelerate_music_path)  # 文件对象必须为 WAV 或 OGG 文件
        self.accelerate_music.set_volume(0.13)

        self.failure_music = pygame.mixer.Sound(self.st.failure_music_path)
        self.failure_music.set_volume(0.13)

        # 火箭初始状态
        self.RK_STATE = 0
        self.RK_SPEED = self.st.MOVE_SPEED

        self.run = self.main_loop
        # 背景
        self._bg = Background(self.screen, self.st)

    # 高度数值显示
    def height_display(self):
        # 字体设置
        self.fontObj = pygame.font.SysFont("simhei", 40)
        # 绘制高度字体
        self.fontTextObj = self.fontObj.render(str(int(self.st.height)), True, (255, 255, 255))
        self.fontRectobj = self.fontTextObj.get_rect()
        self.fontRectobj.centerx = self.st.screen_width / 2
        self.fontRectobj.centery = 50
        self.screen.blit(self.fontTextObj, self.fontRectobj)

    # 按键事件
    def key_event(self):
        # 事件相应处理
        for event in pygame.event.get():
            # 实现窗口退出
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                # 要不要检测空格按下
            if GameSetting.judge_key and GameSetting.key_valid_count > 0:
                # 检测空格是否按下
                if event.type == KEYDOWN:
                    GameSetting.key_valid_count -= 1
                    # 火箭有 6 种状态
                    if event.key == K_SPACE and self.RK_STATE < 6:
                        self.RK_STATE += 1
                        # 加速音效的播放
                        if self.RK_STATE == 1 or self.RK_STATE == 3 or self.RK_STATE == 4 or self.RK_STATE == 6:
                            self.accelerate_music.play()
                            self.st.timer = 0

    def on_draw(self):
        # 绘制固定图层
        self._bg.draw()
        self.height_frame.draw()
        # alter
        if self.st.is_draw_rocket:
            self.rk.draw()
        self.height_display()

        # 判断火箭是否加速，若加速则蓝色火焰维持约 1.5 秒
        if self.st.timer > 1:
            self.st.accelerate = False
        else:
            self.st.timer += 0.01  # 0.01 约等于 clock.tick(100) / 1000
            self.st.accelerate = True

        # 火箭发射后才出现火焰，加速时为蓝色，不加速时为红色
        if self.RK_STATE > 0:
            if self.st.accelerate:
                self.fire.bluefire_draw()
            else:
                self.fire.redfire_draw()

        # 只有当高度为 0 时，才显示火箭发射的提示框
        if self.st.height == 0:
            self.hint_frame.draw(0)

        # 根据高度给定的高度范围，设置相应的提示图
        if GameSetting.key_valid_count and self.st.range0 < self.st.height < self.st.range0_1:
            self.hint_frame.draw(1)
        elif GameSetting.key_valid_count and self.st.range1 < self.st.height < self.st.range1_1:
            self.hint_frame.draw(2)
        elif GameSetting.key_valid_count and self.st.range2 < self.st.height < self.st.range2_1:
            self.hint_frame.draw(3)
        elif GameSetting.key_valid_count and self.st.range3 < self.st.height < self.st.range3_1:
            self.hint_frame.draw(4)
        elif GameSetting.key_valid_count and self.st.range4 < self.st.height < self.st.range4_1:
            self.hint_frame.draw(5)
        if GameSetting.key_valid_count and self.st.game_status == self.st.GAME_LOSE:
            self.failure_music.play()
            self.result.draw(1)
        elif self.st.game_status == self.st.GAME_WIN:
            self.result.draw(0)

    def on_update(self):
        if self.st.game_status == self.st.GAME_INIT:
            delta_time = 0.2
            if self.RK_STATE <= 6:
                # 高度变化
                self.st.height = self.st.height + delta_time * 2 * self._bg.speed
                # 火箭发射
                if self.RK_STATE == 1:
                    self.smoke.draw()
                    # 火箭先移动，背景后移动
                    if self.rk.sv_rect.centery > self.st.screen_height / 2 - 75:
                        self.rk.move()
                        self.fire.fire_move()
                        # 高度变化
                        self.st.height = self.st.height + delta_time * 2 * self.st.MOVE_SPEED
                    else:
                        self.fire.fire_stop()
                        self.smoke.move()
                        self._bg.speed = self.RK_SPEED

                # 抛逃逸塔
                elif self.RK_STATE == 2:
                    self.rk.tower_drop()

                # 助推器分离
                elif self.RK_STATE == 3:
                    self._bg.speed = self.st.ACCELERATE_SPEED * 3
                    self.rk.booster_drop()

                # 一级分离
                elif self.RK_STATE == 4:
                    self._bg.speed = self.st.ACCELERATE_SPEED * 4
                    self.rk.first_drop()
                    self.fire.fire_position(self.st.screen_height / 2 + 15, 0.6)

                # 整流罩分离
                elif self.RK_STATE == 5:
                    self.rk.mask_drop()

                # 船箭分离
                elif self.RK_STATE == 6:
                    self._bg.speed = self.st.ACCELERATE_SPEED * 6
                    self.rk.second_drop()
                    self.fire.fire_position(self.st.screen_height / 2 - 55, 0.5)

            # 以下判断各级分离失败和成功
            # 火箭发射失败或抛逃逸塔失败
            if GameSetting.key_valid_count and (self.st.height > self.st.range0_1 and self.RK_STATE == 1) or (
                    self.st.height < self.st.range0 and self.RK_STATE > 1):
                self.st.game_status = self.st.GAME_LOSE
                GameSetting.judge_key = False
                self._bg.speed = 0
                pygame.mixer.music.stop()

            # 助推器分离失败
            elif GameSetting.key_valid_count and (self.st.height > self.st.range1_1 and self.RK_STATE == 2) or (
                    self.st.height < self.st.range1 and self.RK_STATE > 2):
                self.st.game_status = self.st.GAME_LOSE
                GameSetting.judge_key = False
                self._bg.speed = 0
                pygame.mixer.music.stop()

            # 一级火箭分离失败
            elif GameSetting.key_valid_count and (self.st.height > self.st.range2_1 and self.RK_STATE == 3) or (
                    self.st.height < self.st.range2 and self.RK_STATE > 3):
                self.st.game_status = self.st.GAME_LOSE
                GameSetting.judge_key = False
                self._bg.speed = 0
                pygame.mixer.music.stop()

            # 整流罩分离失败
            elif GameSetting.key_valid_count and (self.st.height > self.st.range3_1 and self.RK_STATE == 4) or (
                    self.st.height < self.st.range3 and self.RK_STATE > 4):
                self.st.game_status = self.st.GAME_LOSE
                GameSetting.judge_key = False
                self._bg.speed = 0
                pygame.mixer.music.stop()

            # 船箭分离失败
            elif GameSetting.key_valid_count and (self.st.height > self.st.range4_1 and self.RK_STATE == 5) or \
                    (self.st.height < self.st.range4 and self.RK_STATE > 5) or \
                    (self.st.range4 < self.st.height < self.st.range4_1 and self.RK_STATE > 6):
                self.st.game_status = self.st.GAME_LOSE
                GameSetting.judge_key = False
                self._bg.speed = 0
                pygame.mixer.music.stop()

            # 任务成功
            elif GameSetting.key_valid_count and self.st.height > self.st.range4_1 and self.RK_STATE == 6:
                self.st.game_status = self.st.GAME_WIN
                GameSetting.judge_key = False
                self._bg.speed = 0

    def main_loop(self):
        self.height_frame = HeightFrame(self.screen, self.st)
        self.hint_frame = HintFrame(self.screen, self.st)
        self.result = ResultImg(self.screen, self.st)

        while True:
            self.key_event()
            self.on_draw()
            self.on_update()
            pygame.display.update()
            pygame.time.delay(10)

    @property
    def bg(self):
        return self.st.bg_name

    @bg.setter
    def bg(self, value):
        self.st.bg_name = value
        self._bg = Background(self.screen, self.st)

    def add(self, sprite):
        self.rk = sprite
        self.smoke = Smoke(self.screen, self.st, self.rk)
        self.fire = Fire(self.screen, self.st)
        # 绘制火箭
        self.st.is_draw_rocket = True


if __name__ == '__main__':
    w = GameWindow()
    w.bg = "bg1.png"
    rk = Rocket()
    rk.color = "blue"
    w.add(rk)
    rk.fly()

    # 设置 '抛逃逸塔' 范围
    rk.et(300, 500)
    # 设置 '助推器分离' 范围
    rk.booster(800, 1000)
    # 设置 "一级分离" 范围
    rk.first(1800, 2200)
    # 设置 "整流罩分离" 范围
    rk.fairing(3000, 3400)
    # 设置 "船箭分离" 范围
    rk.sa(4200, 5200)

    w.run()
