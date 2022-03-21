from math import sin, radians, cos

import pyglet
import numpy


class Enemy:
    def __init__(self, texture, pos_x, pos_y, momentum, dir_x, dir_y):
        self.width = 0
        self.length = 0
        self.set_anchor(texture)
        self.sprite = pyglet.sprite.Sprite(texture, x=pos_x, y=pos_y)
        self.momentum = momentum
        self.dir_y = dir_y
        self.dir_x = dir_x
        self.sprite.x += 0
        self.sprite.y += 0
        self.health = 25

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

    def collision_update(self, x, y, width, length, momentum):
        x_curr_cent = self.sprite.x + self.width / 2
        y_curr_cent = self.sprite.y + self.length / 2

        x_cent = x + width / 2
        y_cent = y + length / 2

        hit = False

        if abs(x_cent - x_curr_cent) < self.width / 2 + width / 2 and abs(
                y_cent - y_curr_cent) < self.length / 2 + length / 2:
            self.momentum = momentum * 0.9
            vec_x = numpy.sign(x_curr_cent - x_cent)
            vec_y = numpy.sign(y_curr_cent - y_cent)
            self.sprite.x += vec_x * momentum / 2
            self.sprite.y += vec_y * momentum / 2
            if vec_y == vec_x:
                self.sprite.rotation -= momentum / 2
            else:
                self.sprite.rotation += momentum / 2
            self.health -= abs(momentum)
            hit = True
        return self.health, hit

    def border_update(self):
        x = self.sprite.x
        y = self.sprite.y
        l = 2 * self.length // 3
        w = self.width // 2
        x += l * sin(radians(self.sprite.rotation))
        y += l * cos(radians(self.sprite.rotation))

        x_r = x + w * sin(radians(self.sprite.rotation - 90))
        x_l = x + w * sin(radians(self.sprite.rotation + 90))

        if x_r > 1440 - self.width:
            self.health -= 0.1
            self.sprite.rotation -= 1
            self.sprite.x -= sin(radians(self.sprite.rotation))

        if x_l < 480 + self.width:
            self.health -= 0.1
            self.sprite.rotation += 1
            self.sprite.x += sin(radians(self.sprite.rotation))

    def update(self, move_y):
        x = self.dir_x
        y = self.dir_y

        if abs(self.momentum) < abs(0.05):
            self.momentum = 0
        y = float(y + self.momentum * 20) / 20.3

        if y:
            self.momentum = y
            self.sprite.rotation += x
            x = y * sin(radians(self.sprite.rotation))
            y = y * cos(radians(self.sprite.rotation))
            self.sprite.x += x
            self.sprite.y += y
        else:
            self.momentum = 0
        self.sprite.y -= move_y
        self.border_update()
        return self.sprite.x > 1920 or self.sprite.y > 3000 or self.sprite.y < -200 or self.sprite.x < 0

    def draw(self):
        self.sprite.draw()
