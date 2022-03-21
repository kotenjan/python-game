import unittest

import Resources
from Boss import Boss
from Enemy import Enemy
from Player import Player
from Rocket import Rocket


class TestCollision(unittest.TestCase):

    def test_enemy_crash_to_car(self):
        player = Player(Resources.player_anim, 720, 300)
        enemy = Enemy(Resources.enemy1_anim, 720, 0, 1, 0, 1)
        for _ in range(120):
            player.update(0, 0)
            enemy.update(0)

        health, hit = enemy.collision_update(player.sprite.x, player.sprite.y, player.width, player.length,
                                             player.momentum)
        self.assertEqual(hit, True, "Collision detection car-enemy, cars did not crash here")

    def test_car_rocket(self):
        player = Player(Resources.player_anim, 720, 300)
        rocket = Rocket(Resources.rocket_anim, 720, 300)
        hit = rocket.collision_update(player.sprite.x, player.sprite.y, player.width, player.length)
        self.assertEqual(hit, True, "Collision detection rocket-enemy, rocket did not crash")

    def test_car_tank(self):
        player = Player(Resources.player_anim, 720, 300)
        boss = Boss(Resources.tank_anim, 720, 300)
        hit = boss.collision_update(player.sprite.x, player.sprite.y, player.width, player.length)
        self.assertEqual(hit, True, "Collision detection tank-enemy, tank did not crash")

    def test_car_road_border(self):
        player = Player(Resources.player_anim, 720, 550)
        player.sprite.rotation = 70
        for _ in range(1000):
            player.update(0, 2)
            player.border_update()
        self.assertLessEqual(player.sprite.rotation, 2, "car is not responding to border on right side")
        player.sprite.rotation = -70
        for _ in range(1000):
            player.update(0, 2)
            player.border_update()
        self.assertGreaterEqual(player.sprite.rotation, -2, "car is not responding to border on left side")

    def test_two_enemies(self):
        enemy2 = Enemy(Resources.enemy1_anim, 500, 0, 1, 0, 2)
        enemy2.sprite.rotation = 20
        enemy1 = Enemy(Resources.enemy1_anim, 600, 0, 1, 0, 2)
        enemy1.sprite.rotation = -20
        for _ in range(1000):
            enemy1.update(0)
            enemy1.collision_update(enemy2.sprite.x, enemy2.sprite.y, enemy2.width, enemy2.length, enemy2.momentum)
            enemy2.update(0)
            enemy2.collision_update(enemy1.sprite.x, enemy1.sprite.y, enemy1.width, enemy1.length, enemy1.momentum)

        self.assertGreaterEqual(0, enemy1.sprite.rotation, "enemy is not responding to other enemy collision")
        self.assertLessEqual(0, enemy2.sprite.rotation, "enemy is not responding to other enemy collision")

    def test_car_crash_to_enemy(self):
        player = Player(Resources.player_anim, 720, 300)
        enemy = Enemy(Resources.enemy1_anim, 700, 500, 0, 0, 1)
        for _ in range(1000):
            player.update(0, 2)
            enemy.collision_update(player.sprite.x, player.sprite.y, player.width, player.length, player.momentum)
            enemy.update(0)

        enemy.collision_update(player.sprite.x, player.sprite.y, player.width, player.length, player.momentum)
        self.assertNotEqual(enemy.sprite.rotation, 0, "enemy did not change rotation upon side collision")

    def test_enemy_border(self):
        enemy = Enemy(Resources.enemy1_anim, 720, 0, 5, 0, 1)
        enemy.health = 1000000
        enemy.sprite.rotation = 70
        for _ in range(1000):
            enemy.update(0)
            enemy.border_update()
            enemy.momentum = 1
        self.assertLessEqual(enemy.sprite.rotation, 50, "enemy is not responding to border on right side")
        enemy.sprite.rotation = -70
        for _ in range(1000):
            enemy.update(0)
            enemy.border_update()
            enemy.momentum = 1
        self.assertGreaterEqual(enemy.sprite.rotation, -50, "enemy is not responding to border on left side")
