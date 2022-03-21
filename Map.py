import pyglet


class Map:
    def __init__(self, starting_texture, texture, *args):
        self.texture = texture
        self.momentum = 0
        self.map = list()
        self.scenery = args
        self.map.append(pyglet.sprite.Sprite(starting_texture, x=0, y=0))
        self.map.append(pyglet.sprite.Sprite(texture, x=0, y=texture.height))
        self.map.append(pyglet.sprite.Sprite(texture, x=0, y=texture.height * 2))

    def update(self, y):
        remove = False
        destination = 0

        for tile in self.map:
            tile.y -= y
            if tile.y < -tile.height:
                remove = True
                destination = tile.y

        if remove:
            self.map.pop(0)
            self.map.append(pyglet.sprite.Sprite(self.texture, x=0, y=self.texture.height * 2 + destination))

    def draw(self):
        for x in self.map:
            x.draw()
