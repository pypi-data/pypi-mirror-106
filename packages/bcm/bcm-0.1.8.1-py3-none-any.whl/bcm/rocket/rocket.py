import pygame
import os
from .parameter_setting import GameSetting


class Rocket:
    def __init__(self):
        self.setting = GameSetting()
        self.screen = self.setting.screen

        # 加载火箭
        self.load_rocket()

        self.angle_drop = 1
        self.angle_push1 = 1
        self.angle_push2 = 1
        self.angle_push3 = 1
        self.angle_push4 = 1
        self.angle_first = 1
        self.angle_mask1 = 1
        self.angle_mask2 = 1
        self.angle_second = 1

    def load_rocket(self):
        self.compose_list = []  # 航天器图片对象
        self.rect_list = []  # 航天器矩形对象
        # 航天器
        self.sv = pygame.image.load(self.setting.space_vehicle_path)
        self.sv = pygame.transform.smoothscale(self.sv, (int(356 * 0.1), int(856 * 0.1)))
        self.compose_list.append(self.sv)
        self.sv_rect = self.sv.get_rect()
        self.rect_list.append(self.sv_rect)
        self.sv_rect.center = (self.setting.screen_width / 2 + 1, self.setting.screen_height / 2 + 40)

        # 逃逸塔
        self.tower = pygame.image.load(self.setting.tower_path)
        self.tower = pygame.transform.smoothscale(self.tower, (int(263 * 0.15), int(301 * 0.15)))
        self.compose_list.append(self.tower)
        self.tower_rect = self.tower.get_rect()

        self.tower_rect.center = (self.setting.screen_width / 2, self.sv_rect.centery - self.sv_rect.height / 2 - 10)
        self.rect_list.append(self.tower_rect)

        # 整流罩(右侧)
        self.mask1 = pygame.image.load(self.setting.mask1_path)
        self.mask1 = pygame.transform.smoothscale(self.mask1, (int(179 * 0.11), int(731 * 0.11)))
        self.compose_list.append(self.mask1)
        self.mask1_rect = self.mask1.get_rect()
        self.rect_list.append(self.mask1_rect)
        self.mask1_rect.center = (self.setting.screen_width / 2 + 9, self.sv_rect.centery)

        # 整流罩(左侧)
        self.mask2 = pygame.image.load(self.setting.mask2_path)
        self.mask2 = pygame.transform.smoothscale(self.mask2, (int(179 * 0.11), int(731 * 0.11)))
        self.compose_list.append(self.mask2)
        self.mask2_rect = self.mask2.get_rect()
        self.rect_list.append(self.mask2_rect)
        self.mask2_rect.center = (self.setting.screen_width / 2 - 9, self.sv_rect.centery)

        # 二级火箭
        self.second = pygame.image.load(self.setting.second_path)
        self.second = pygame.transform.smoothscale(self.second, (int(492 * 0.1), int(835 * 0.1)))
        self.compose_list.append(self.second)
        self.second_rect = self.second.get_rect()
        self.rect_list.append(self.second_rect)
        self.second_rect.center = (self.setting.screen_width / 2 + 2.5,
                                   self.sv_rect.centery + self.sv_rect.height / 2 + self.second_rect.height / 2 - 13)

        # 助推器（后）
        self.push4 = pygame.image.load(self.setting.push4_path)
        self.push4 = pygame.transform.smoothscale(self.push4, (int(289 * 0.07), int(1044 * 0.07)))
        self.compose_list.append(self.push4)
        self.push4_rect = self.push4.get_rect()
        self.rect_list.append(self.push4_rect)
        self.push4_rect.center = (self.setting.screen_width / 2 + 2, self.sv_rect.bottom + self.second_rect.height + 42)

        # 一级火箭
        self.first_ = pygame.image.load(self.setting.first_path)
        self.first_ = pygame.transform.smoothscale(self.first_, (int(361 * 0.1), int(1469 * 0.1)))
        self.compose_list.append(self.first_)
        self.first_rect = self.first_.get_rect()
        self.rect_list.append(self.first_rect)
        self.first_rect.center = (self.setting.screen_width / 2 + 1.8,
                                  self.sv_rect.centery + self.sv_rect.height / 2 + self.second_rect.height + self.first_rect.height / 2 - 42)

        # 助推器（左）
        self.push1 = pygame.image.load(self.setting.push1_path)
        self.push1 = pygame.transform.smoothscale(self.push1, (int(385 * 0.1), int(1026 * 0.1)))
        self.compose_list.append(self.push1)
        self.push1_rect = self.push1.get_rect()
        self.rect_list.append(self.push1_rect)
        self.push1_rect.center = (
            self.setting.screen_width / 2 - 25, self.sv_rect.bottom + self.second_rect.height + 42)

        # 助推器（中）
        self.push2 = pygame.image.load(self.setting.push2_path)
        self.push2 = pygame.transform.smoothscale(self.push2, (int(289 * 0.11), int(1044 * 0.11)))
        self.compose_list.append(self.push2)
        self.push2_rect = self.push2.get_rect()
        self.rect_list.append(self.push2_rect)
        self.push2_rect.center = (self.setting.screen_width / 2 + 2, self.sv_rect.bottom + self.second_rect.height + 42)

        # 助推器（右）
        self.push3 = pygame.image.load(self.setting.push3_path)
        self.push3 = pygame.transform.smoothscale(self.push3, (int(403 * 0.1), int(1092 * 0.1)))
        self.compose_list.append(self.push3)
        self.push3_rect = self.push3.get_rect()
        self.rect_list.append(self.push3_rect)
        self.push3_rect.center = (
            self.setting.screen_width / 2 + 29, self.sv_rect.bottom + self.second_rect.height + 44)

    def draw(self):
        for i in range(len(self.compose_list)):
            self.screen.blit(self.compose_list[i], self.rect_list[i])

    def move(self):
        if self.sv_rect.centery < self.setting.screen_height / 2 - 75:
            for i in self.rect_list:
                i.centery -= 0
        else:
            for i in self.rect_list:
                i.centery -= self.setting.MOVE_SPEED

    def tower_drop(self):
        # 旋转
        self.newtower = pygame.transform.rotate(self.tower, self.angle_drop)
        self.rect_list[1] = self.newtower.get_rect(center=self.tower_rect.center)
        self.compose_list[1] = self.newtower
        self.angle_drop += 3

        # 坐标变化
        self.tower_rect.centery += self.setting.fail_speed * 3
        self.tower_rect.centerx -= self.setting.fail_speed * 0.004
        if self.tower_rect.centery > self.setting.screen_height or self.tower_rect.centerx > self.setting.screen_width:
            self.tower_rect.centery += 0
            self.tower_rect.centerx -= 0

    def booster_drop(self):
        self.newpush1 = pygame.transform.rotate(self.push1, self.angle_push1)
        self.rect_list[7] = self.newpush1.get_rect(center=self.push1_rect.center)
        self.compose_list[7] = self.newpush1
        self.angle_push1 += 6
        self.push1_rect.centery += self.setting.fail_speed * 2.7
        self.push1_rect.centerx -= self.setting.fail_speed * 1.02
        if self.push1_rect.centery > self.setting.screen_height or self.push1_rect.centerx > self.setting.screen_width:
            self.push1_rect.centery += 0
            self.push1_rect.centerx -= 0

        self.newpush2 = pygame.transform.rotate(self.push2, self.angle_push2)
        self.rect_list[8] = self.newpush2.get_rect(center=self.push2_rect.center)
        self.compose_list[8] = self.newpush2
        self.angle_push2 += 6
        self.push2_rect.centery += self.setting.fail_speed * 2.1
        self.push2_rect.centerx -= self.setting.fail_speed * 0.0001
        if self.push2_rect.centery > self.setting.screen_height or self.push2_rect.centerx > self.setting.screen_width:
            self.push2_rect.centery += 0
            self.push2_rect.centerx -= 0

        self.newpush3 = pygame.transform.rotate(self.push3, self.angle_push3)
        self.rect_list[9] = self.newpush3.get_rect(center=self.push3_rect.center)
        self.compose_list[9] = self.newpush3
        self.angle_push3 -= 6
        self.push3_rect.centerx += self.setting.fail_speed * 1.6
        self.push3_rect.centery += self.setting.fail_speed * 2
        if self.push3_rect.centery > self.setting.screen_height or self.push3_rect.centerx > self.setting.screen_width:
            self.push3_rect.centery += 0
            self.push3_rect.centerx += 0

        self.newpush4 = pygame.transform.rotate(self.push4, self.angle_push4)
        self.rect_list[5] = self.newpush4.get_rect(center=self.push4_rect.center)
        self.compose_list[5] = self.newpush4
        self.angle_push4 -= 6
        self.push4_rect.centerx += self.setting.fail_speed * 0.8
        self.push4_rect.centery += self.setting.fail_speed * 2
        if self.push4_rect.centery > self.setting.screen_height or self.push4_rect.centerx > self.setting.screen_width:
            self.push4_rect.centery += 0
            self.push4_rect.centerx += 0

    def first_drop(self):
        self.newfirst = pygame.transform.rotate(self.first_, self.angle_first)
        self.rect_list[6] = self.newfirst.get_rect(center=self.first_rect.center)
        self.compose_list[6] = self.newfirst
        self.angle_first -= 2
        self.first_rect.centerx -= self.setting.fail_speed * 0.3
        self.first_rect.centery += self.setting.fail_speed * 2.5
        if self.first_rect.centery > self.setting.screen_height or self.first_rect.centerx > self.setting.screen_width:
            self.first_rect.centery += 0
            self.first_rect.centerx += 0

    def mask_drop(self):
        self.newmask1 = pygame.transform.rotate(self.mask1, self.angle_mask1)
        self.rect_list[2] = self.newmask1.get_rect(center=self.mask1_rect.center)
        self.compose_list[2] = self.newmask1
        self.angle_mask1 -= 5
        self.mask1_rect.centerx += self.setting.fail_speed * 1
        self.mask1_rect.centery += self.setting.fail_speed * 2.6
        if self.mask1_rect.centery > self.setting.screen_height or self.mask1_rect.centerx > self.setting.screen_width:
            self.mask1_rect.centery += 0
            self.mask1_rect.centerx += 0

        self.newmask2 = pygame.transform.rotate(self.mask2, self.angle_mask2)
        self.rect_list[3] = self.newmask2.get_rect(center=self.mask2_rect.center)
        self.compose_list[3] = self.newmask2
        self.angle_mask2 += 5
        self.mask2_rect.centerx -= self.setting.fail_speed * 0.007
        self.mask2_rect.centery += self.setting.fail_speed * 2.6
        if self.mask2_rect.centery > self.setting.screen_height or self.mask2_rect.centerx > self.setting.screen_width:
            self.mask2_rect.centery += 0
            self.mask2_rect.centerx += 0

    def second_drop(self):
        self.newsecond = pygame.transform.rotate(self.second, self.angle_second)
        self.rect_list[4] = self.newsecond.get_rect(center=self.second_rect.center)
        self.compose_list[4] = self.newsecond
        self.angle_second -= 4
        self.second_rect.centerx += self.setting.fail_speed * 0.9
        self.second_rect.centery += self.setting.fail_speed * 2.1
        if self.second_rect.centery > self.setting.screen_height or self.second_rect.centerx > self.setting.screen_width:
            self.second_rect.centery += 0
            self.second_rect.centerx += 0

    def fly(self):
        GameSetting.judge_key = True

    @property
    def color(self):
        return self.setting.rk_color

    @color.setter
    def color(self, value):
        self.setting.rk_color = value
        self.load_rocket()

    # 高度
    def et(self, range_left, range_right):
        if range_right > range_left:
            self.setting.range0, self.setting.range0_1 = range_left, range_right
            GameSetting.key_valid_count += 1
        else:
            raise RuntimeError("设置的高度范围不正确")

    def booster(self, range_left, range_right):
        if range_right > range_left:
            self.setting.range1, self.setting.range1_1 = range_left, range_right
            GameSetting.key_valid_count += 1
        else:
            raise RuntimeError("设置的高度范围不正确")

    def first(self, range_left, range_right):
        if range_right > range_left:
            self.setting.range2, self.setting.range2_1 = range_left, range_right
            GameSetting.key_valid_count += 1
        else:
            raise RuntimeError("设置的高度范围不正确")

    def fairing(self, range_left, range_right):
        if range_right > range_left:
            self.setting.range3, self.setting.range3_1 = range_left, range_right
            GameSetting.key_valid_count += 1
        else:
            raise RuntimeError("设置的高度范围不正确")

    def sa(self, range_left, range_right):
        if range_right > range_left:
            self.setting.range4, self.setting.range4_1 = range_left, range_right
            GameSetting.key_valid_count += 1
        else:
            raise RuntimeError("设置的高度范围不正确")


# 火焰
class Fire:
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting
        self.scale = 1
        self.fire_list = []
        self.fire_list_copy = []
        for i in range(6):
            self.rawimage = pygame.image.load(f"{self.setting.fire_path}{os.sep}fire{i + 1}.png")
            self.rawimage = pygame.transform.scale(self.rawimage, (int(140 * self.scale), int(100 * self.scale)))
            self.fire_list.append(self.rawimage)
            self.fire_list_copy.append(self.rawimage)

        self.rect = self.rawimage.get_rect()  # 得到原始图的数据
        self.rect.centerx = self.setting.screen_width / 2 - 1.6
        self.rect.top = self.setting.screen_height / 2 + 218
        self.idx = 0
        self.position = 0

    def redfire_draw(self):
        self.screen.blit(self.fire_list[self.idx % 3], self.rect)
        self.idx += 1

    def bluefire_draw(self):
        self.screen.blit(self.fire_list[self.idx % 3 + 3], self.rect)
        self.idx += 1

    def fire_move(self):
        self.rect.top -= self.setting.MOVE_SPEED

    def fire_stop(self):
        self.rect.top -= 0

    def fire_position(self, position, scale):
        self.fire_list = []
        for i in range(6):
            self.image = pygame.transform.scale(self.fire_list_copy[i], (int(140 * scale), int(100 * scale)))
            self.fire_list.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.centerx = self.setting.screen_width / 2 - 1.6
        self.rect.top = position
