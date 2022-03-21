import pyglet
from random import randint


class Health:
    def __init__(self, texture, health):
        self.width = 0
        self.length = 0
        self.set_anchor(texture)
        self.sprite = pyglet.sprite.Sprite(texture, x=randint(1, 832) + 544, y=randint(1080, 4000) + 1080)
        self.sprite.x += 0
        self.sprite.y += 0
        self.health = health

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

    def update(self, x, y, width, length, move_y):
        self.sprite.y -= move_y
        x_curr_cent = self.sprite.x + self.width / 2
        y_curr_cent = self.sprite.y + self.length / 2

        x_cent = x + width / 2
        y_cent = y + length / 2

        if abs(x_cent - x_curr_cent) < self.width + width / 2 and abs(
                y_cent - y_curr_cent) < self.length + length / 2:
            self.sprite.x = randint(1, 832) + 544
            self.sprite.y = randint(1080, 4000) + 1080
            return self.health
        if self.sprite.y < -200:
            self.sprite.x = randint(1, 832) + 544
            self.sprite.y = randint(1080, 4000) + 1080
        return 0

    def draw(self):
        if self.sprite.y < 1100:
            self.sprite.draw()
