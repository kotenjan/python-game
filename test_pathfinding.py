import unittest
from math import degrees, atan2

import Resources
from Boss import Boss
from Player import Player
from Rocket import Rocket


class TestPathfinding(unittest.TestCase):

    def test_car_tank(self):
        player = Player(Resources.player_anim, 1090, 300)
        boss = Boss(Resources.tank_anim, 0, -3500)
        boss.sprite.rotation = -30
        for _ in range(300):
            boss.update(0, player.sprite.x, player.sprite.y)
        x = player.sprite.x - boss.sprite.x
        y = player.sprite.y - boss.sprite.y
        self.assertAlmostEqual(-degrees(atan2(-x, y)), boss.sprite.rotation, delta=10,
                               msg="tank is not turned towards player")

    def test_car_rocket(self):
        player = Player(Resources.player_anim, 1090, 300)
        rocket = Rocket(Resources.tank_anim, 0, -6500)
        rocket.sprite.rotation = -30
        for _ in range(1):
            rocket.update(0, player.sprite.x, player.sprite.y, rocket.sprite.x, -8000)
        x = player.sprite.x - rocket.sprite.x
        y = player.sprite.y - rocket.sprite.y
        self.assertGreater(rocket.sprite.rotation, -30, msg="rocket is not turned towards player")
