from math import sin, radians, cos

import pyglet


class Particle:
    def __init__(self, texture, pos_x, pos_y, momentum, dir_x, dir_y, timestamp=1000):
        self.sprite = pyglet.sprite.Sprite(texture, x=pos_x, y=pos_y)
        self.sprite.x += 0
        self.sprite.y += 0
        self.set_anchor(texture)
        self.momentum = momentum
        self.dir_y = dir_y
        self.dir_x = dir_x
        self.timestamp = timestamp

    def set_anchor(self, texture):
        if isinstance(texture, pyglet.image.Animation):
            for f in texture.frames:
                f.image.anchor_x = f.image.width // 2
                f.image.anchor_y = f.image.height // 3
        else:
            texture.anchor_x = texture.width // 2
            texture.anchor_y = texture.height // 3

    def add_batch(self, batch):
        self.sprite.batch = batch

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
        self.timestamp -= 1
        return self.sprite.x > 1920 or self.sprite.y > 1920 or self.sprite.y < 0 or self.sprite.x < 0 or self.timestamp <= 0

    def draw(self):
        self.sprite.draw()
