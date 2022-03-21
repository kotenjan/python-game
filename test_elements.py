import unittest

import Resources
from Bar import Bar
from Boss import Boss
from Enemies import Enemies
from Enemy import Enemy
from Particle import Particle
from Particles import Particles
from Player import Player
from Rocket import Rocket


class TestCollision(unittest.TestCase):

    def test_bar_limit(self):
        health_bar = Bar(Resources.health_bar, Resources.health_bar_bit, 10, 10, 125)
        health_bar.update(4000)
        self.assertLessEqual(health_bar.vitality, health_bar.capacity, "bar has no limit")

    def test_tank_movement(self):
        thing = Boss(Resources.tank_anim, 0, -3500)
        thing.sprite.rotation = -30
        for _ in range(10):
            thing.update(0, 300, 1)
        self.assertLess(-3500, thing.sprite.y, "Tank is not moving")
        self.assertLess(-30, thing.sprite.x, "Rocket is not moving to sides")

    def test_rocket_movement(self):
        thing = Rocket(Resources.rocket_anim, -300, -6000)
        thing.sprite.rotation = -3
        for _ in range(3):
            thing.update(0, 0, 0, 8000, -800)
        self.assertLess(-6000, thing.sprite.y, "Rocket is not moving forward")
        self.assertLess(-3, thing.sprite.x, "Rocket is not moving to sides")

    def test_player_movement(self):
        player = Player(Resources.player_anim, 720, 300)
        for _ in range(25):
            player.update(1, 1)
        self.assertGreater(player.sprite.x, 720, "player not moving forward")
        self.assertGreater(player.sprite.y, 310, "player not moving to sides")

    def test_enemy_movement(self):
        enemy = Enemy(Resources.enemy1_anim, 720, 0, 1, 0, 1)
        enemy.sprite.rotation = 10
        for _ in range(25):
            enemy.update(0)
        self.assertGreater(enemy.sprite.x, 720, "enemy not moving forward")
        self.assertGreater(enemy.sprite.y, 0, "enemy not moving to sides")

    def test_enemy_removing(self):
        enemies = Enemies()
        enemy2 = Enemy(Resources.enemy1_anim, 500, 0, 1, 0, 2)
        enemy1 = Enemy(Resources.enemy1_anim, 600, 0, 1, 0, 2)
        enemy1.health = -20
        enemies.append(enemy1)
        enemies.append(enemy2)
        particles = list()
        enemies.update(0, particles)
        self.assertEqual(len(enemies.map), 1, "Dead enemy not removed")

    def test_particle_removing(self):
        particles = Particles()
        particle2 = Particle(Resources.enemy1_anim, 500, 0, 1, 0, 2, 100)
        particle1 = Particle(Resources.enemy1_anim, 600, 0, 1, 0, 2, 100)
        particles.append(particle1)
        particles.append(particle2)
        for _ in range(102):
            particles.update(0)
        self.assertEqual(len(particles.map), 0, "Dead enemy not removed")
