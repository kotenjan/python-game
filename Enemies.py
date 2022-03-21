import random

import Resources
from Particle import Particle


class Enemies:
    def __init__(self):
        self.momentum = 0
        self.map = list()

    def append(self, enemy):
        self.map.append(enemy)

    def update(self, y, particles):
        for enemy in self.map:
            for reference in self.map:
                if enemy is not reference:
                    reference.collision_update(enemy.sprite.x, enemy.sprite.y, enemy.width, enemy.length,
                                               enemy.momentum)

        for enemy in self.map:
            if enemy.health <= 0:
                particles.append(Particle(Resources.fire_car_anim, enemy.sprite.x,
                                          enemy.sprite.y, 10, (random.random() - 0.5) * 6,
                                          (random.random() - 0.5), 45))
                self.map.remove(enemy)
            else:
                if enemy.update(y):
                    self.map.remove(enemy)

    def update_collision(self, player):
        for reference in self.map:
            health, hit = reference.collision_update(player.sprite.x, player.sprite.y, player.width,
                                                     player.length, player.momentum)
            if hit:
                player.health -= abs(player.momentum)
                player.momentum *= 0.6

    def update_boss_collision(self, player):
        for reference in self.map:
            reference.collision_update(player.sprite.x, player.sprite.y, player.width, player.length, 100)

    def draw(self):
        for x in self.map:
            x.draw()
