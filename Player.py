from math import sin, radians, cos

import pyglet
import numpy


class Player:
    def __init__(self, texture, pos_x, pos_y):
        self.width = 0
        self.length = 0
        self.set_anchor(texture)
        self.sprite = pyglet.sprite.Sprite(texture, x=pos_x, y=pos_y)
        self.momentum = 0
        self.sprite.x += 0
        self.sprite.y += 0
        self.break_factor = 1
        self.speed_factor = 1
        self.health = 125
        self.stamina = 800
        self.recharging = False
        self.score = 0

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

    def border_update(self):
        x = self.sprite.x
        y = self.sprite.y
        l = 2 * self.length // 3
        w = self.width // 2
        x += l * sin(radians(self.sprite.rotation))
        y += l * cos(radians(self.sprite.rotation))

        x_r = x + w * sin(radians(self.sprite.rotation - 90))
        x_l = x + w * sin(radians(self.sprite.rotation + 90))

        if x_r > 1440 - self.width + 40:
            self.sprite.rotation -= (x_r - (1440 - self.width + 40)) / 2
            self.sprite.x -= sin(radians(self.sprite.rotation))
            self.momentum *= 0.9
        if x_l < 480 + self.width - 40:
            self.sprite.rotation -= (x_l - (480 + self.width - 40)) / 2
            self.sprite.x -= sin(radians(self.sprite.rotation))
            self.momentum *= 0.9

    def update(self, x, y):
        map_move = 0

        if abs(x) > 1 or abs(y) > 1:
            if self.stamina > 0 and not self.recharging:
                self.stamina -= 3.5
            else:
                self.recharging = True
                x = numpy.sign(x)
                y = numpy.sign(y)

        if self.stamina > 350 and self.recharging:
            self.recharging = False

        self.stamina += 2

        self.health = min(self.health, 125)
        self.stamina = min(self.stamina, 1000)

        if y < 0:
            y *= self.break_factor

        if y > 0:
            y *= self.speed_factor

        if abs(self.momentum) < abs(0.05):
            self.momentum = 0
        y = float(y + self.momentum * 10) / 10.2

        if y:
            self.momentum = y
            self.sprite.rotation += x * (min(abs(y), 1) + 0.5)
            x = y * sin(radians(self.sprite.rotation))
            y = y * cos(radians(self.sprite.rotation))
            self.sprite.x += x
            if y > 0:
                map_move = min(self.sprite.y / 540, 1) * y
            self.score += y / 100
            self.sprite.y += y - map_move
        else:
            self.momentum = 0
        self.border_update()
        return map_move

    def draw(self):
        self.sprite.draw()

    def y(self):
        return self.sprite.y

    def get_tire_pos(self):
        tires = list()
        tires.append((self.sprite.x - 10, self.sprite.y - 10))
        tires.append((self.sprite.x + self.width - 10, self.sprite.y + self.length - 10))
        tires.append((self.sprite.x + self.width - 10, self.sprite.y - 10))
        tires.append((self.sprite.x - 10, self.sprite.y + self.length - 10))
        return tires
