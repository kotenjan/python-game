from math import sin, radians, cos, degrees, atan2

import pyglet
import numpy
from random import randint


class Rocket:
    def __init__(self, texture, pos_x, pos_y):
        self.width = 0
        self.length = 0
        self.set_anchor(texture)
        self.sprite = pyglet.sprite.Sprite(texture, x=pos_x, y=pos_y)
        self.momentum = 20
        self.sprite.x += 0
        self.sprite.y += 0
        self.dir_x = 0
        self.dir_y = 1
        self.speed_factor = 0

    def set_anchor(self, texture):
        if isinstance(texture, pyglet.image.Animation):
            self.width = texture.frames[0].image.width
            self.length = texture.frames[0].image.height
            for f in texture.frames:
                f.image.anchor_x = f.image.width // 2
                f.image.anchor_y = f.image.height // 3
        else:
            texture.anchor_x = texture.width // 2
            texture.anchor_y = texture.height // 3
            self.width = texture.width
            self.length = texture.height

    def add_batch(self, batch):
        self.sprite.batch = batch

    def collision_update(self, x, y, width, length):
        x_curr_cent = self.sprite.x + self.width / 2
        y_curr_cent = self.sprite.y + self.length / 2

        x_cent = x + width / 2
        y_cent = y + length / 2

        if abs(x_cent - x_curr_cent) < self.width / 2.2 + width / 2 and abs(
                y_cent - y_curr_cent) < self.length / 2.2 + length / 2:
            return True
        return False

    def update(self, move_y, x_pos, y_pos, tank_x, tank_y):

        if self.sprite.y < tank_y:
            self.sprite.x = tank_x
        if self.sprite.y > 1500 or (tank_y > -500 and self.sprite.y < tank_y):
            self.sprite.y = tank_y - 6000 - randint(1000, 6000)
            self.sprite.rotation = 0

        x = x_pos - self.sprite.x
        y = y_pos - self.sprite.y

        degree = -degrees(atan2(-x, y))

        x = numpy.sign(int((degree - self.sprite.rotation)))

        self.sprite.rotation += x / 20
        x = self.momentum * sin(radians(self.sprite.rotation))
        y = self.momentum * cos(radians(self.sprite.rotation))
        self.sprite.x += x
        self.sprite.y += y
        self.sprite.y -= move_y

    def draw(self):
        if self.sprite.y > -160:
            self.sprite.draw()
