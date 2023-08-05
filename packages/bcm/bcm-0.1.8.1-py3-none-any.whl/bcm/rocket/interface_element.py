import pygame
import os

# 背景
class Background:
    def __init__(self, screen, setting):
        self.sc = screen
        # 载入：构建背景素材列表
        self.bg_list = []
        bg_bt_temp = pygame.image.load(setting.bg_bottom_path)
        bg_top_temp = pygame.image.load(setting.bg_top_path)
        self.bg_list.append([bg_bt_temp, bg_top_temp])
        self.speed = 0
        self.bg_hight = 0
        self.out = 0

    def draw(self):
        """
        情况一：
        火箭还未发射，speed为0 - 贴图为背景、山、发射塔
        情况二：
        火箭发射，speed不为0，但是初始图片未退出窗口bg_hight<650 - 贴图为背景、山、发射塔、星空
        情况三：
        火箭发射，speed不为0，且初始图片退出窗口 bg_hight>=650 - 贴图为星空
        """
        self.cur_bg = self.bg_list[0]
        self.bg_hight = self.bg_hight + self.speed
        if self.out != 1:
            # 贴背景、山、发射塔
            self.sc.blit(self.cur_bg[0], (0, -650 + self.bg_hight))
            if self.bg_hight >= 650:
                self.out = 1
                self.bg_hight = 0
        else:
            self.sc.blit(self.cur_bg[1], (0, -650 + self.bg_hight))
            if self.bg_hight >= 650:
                self.bg_hight = 0


# 高度显示框
class HeightFrame:
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting
        self.image = pygame.image.load(self.setting.height_frame_path)
        self.image = pygame.transform.smoothscale(self.image, (int(181 * 0.8), int(84 * 0.8)))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.setting.screen_width / 2
        self.rect.centery = 50

    def draw(self):
        self.screen.blit(self.image, self.rect)


# 游戏提示框
class HintFrame:
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting
        self.hint_list = []
        for i in range(6):
            temp = pygame.image.load(self.setting.rk_state_path[i])
            temp = pygame.transform.smoothscale(temp, (int(751 * 0.2), int(295 * 0.2)))
            self.hint_list.append(temp)
        self.rect = temp.get_rect()
        self.rect.centerx = self.setting.screen_width / 2
        self.rect.centery = 140

    def draw(self, st_num):
        self.screen.blit(self.hint_list[st_num], self.rect)


# 游戏结果图
class ResultImg:
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting
        self.res_img = []
        self.temp = pygame.image.load(self.setting.result_win_path)
        self.temp = pygame.transform.smoothscale(self.temp, (int(888 * 0.4), int(800 * 0.4)))
        self.res_img.append(self.temp)
        self.temp = pygame.image.load(self.setting.result_lose_path)
        self.temp = pygame.transform.smoothscale(self.temp, (int(888 * 0.4), int(800 * 0.4)))
        self.res_img.append(self.temp)

        self.rect = self.temp.get_rect()
        self.rect.centerx = self.setting.screen_width / 2
        self.rect.centery = self.setting.screen_height / 2

    def draw(self, game_state):
        self.screen.blit(self.res_img[game_state], self.rect)


# 烟雾
class Smoke:
    def __init__(self, screen, setting, rk):
        self.screen = screen
        self.setting = setting
        self.rk = rk
        self.smoke_list = []
        for i in range(4):
            self.smoke_list.append(pygame.image.load(f"{self.setting.smoke_path}{os.sep}smoke{i + 1}.png"))
        self.image = self.smoke_list[0]
        self.image = pygame.transform.smoothscale(self.image, (int(1280 * 1.2), int(720 * 1.2)))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.setting.screen_width / 2 + 90
        self.rect.bottom = self.setting.screen_height + 260
        self.idx = 0

    def draw(self):
        self.screen.blit(self.smoke_list[self.idx % 3], self.rect)
        self.idx += 1

    def move(self):
        self.rect.top += self.setting.MOVE_SPEED
        if self.rect.top > self.setting.screen_height:
            self.rect.top = self.setting.screen_height
