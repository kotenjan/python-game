import pyglet


class Bar:
    def __init__(self, texture, bar_bit, pos_x, pos_y, capacity):
        self.sprite = pyglet.sprite.Sprite(texture, x=pos_x, y=pos_y)
        self.bar_bit = bar_bit
        self.set_anchor(texture)
        self.capacity = capacity
        self.vitality = 0
        self.sprite.x += 0
        self.sprite.y += 0

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

    def update(self, vitality):
        vitality = min(vitality, self.capacity)
        full = self.sprite.width // self.bar_bit.width
        full *= (vitality / self.capacity)
        self.vitality = int(full)

    def draw(self):
        self.sprite.draw()
        for i in range(self.vitality):
            pyglet.sprite.Sprite(self.bar_bit, x=self.sprite.x + i * self.bar_bit.width, y=self.sprite.y).draw()
