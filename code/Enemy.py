#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__('Enemy3', (x, y))
        self.vel_y = 2
        self.direction_y = 1
        self.vel_x = -ENTITY_SPEED['Enemy3']

    def move(self):
        self.rect.x += self.vel_x
        if self.rect.right < 0:
            pass

        self.rect.y += self.vel_y * self.direction_y

        if self.rect.bottom >= WIN_HEIGHT:
            self.direction_y = -1
            self.vel_y = 2
        elif self.rect.top <= 0:
            self.direction_y = 1
            self.vel_y *= 2

    def shoot(self):
        if pygame.time.get_ticks() % ENTITY_SHOT_DELAY['Enemy3'] == 0:
            return EnemyShot(name='Enemy3Shot', position=(self.rect.centerx, self.rect.centery))
        return None