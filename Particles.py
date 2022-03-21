class Particles:

    def __init__(self):
        self.momentum = 0
        self.map = list()

    def append(self, particle):
        self.map.append(particle)

    def update(self, y):
        for particle in self.map:
            if particle.update(y):
                self.map.remove(particle)

    def draw(self):
        for x in self.map:
            x.draw()
