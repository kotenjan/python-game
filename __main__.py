import Resources
from Bar import Bar
from Boss import Boss
from Enemies import Enemies
from Enemy import Enemy
from Health import Health
from Map import Map
from Player import Player
from Particles import Particles
from Particle import Particle
import pyglet
from pyglet.window import key
from random import randint

from Rocket import Rocket

window = pyglet.window.Window(caption="Road Rage", resizable=False, fullscreen=True)
main_batch = pyglet.graphics.Batch()

x_movement = 0
y_movement = 0
shift = False
space = False

death = False
menu = False

enemy_counter = 0

tiles = list()


@window.event
def on_key_press(symbol, modifiers):
    global y_movement, x_movement, space
    if symbol == key.RIGHT:
        x_movement = 1
    if symbol == key.LEFT:
        x_movement = -1
    if symbol == key.UP:
        y_movement = 1
    if symbol == key.DOWN:
        y_movement = -1
    if symbol == key.SPACE:
        space = True


@window.event
def on_key_release(symbol, modifiers):
    global y_movement, x_movement, space, menu, death, shift
    if symbol == key.RIGHT:
        x_movement = 0
    if symbol == key.LEFT:
        x_movement = 0
    if symbol == key.UP:
        y_movement = 0
    if symbol == key.DOWN:
        y_movement = 0
    if symbol == key.SPACE:
        space = False
    if symbol == key.P:
        menu = not menu
        if death:
            x_movement = 0
            y_movement = 0
            shift = False
            space = False
            death = False
            menu = False
            restart()


@window.event
def on_draw():
    global menu, death
    window.clear()
    game_map.draw()
    player.draw()
    enemies.draw()
    if rocket.sprite.y > boss.sprite.y:
        rocket.draw()
    boss.draw()
    particles.draw()
    heart.draw()
    health_bar.draw()
    stamina_bar.draw()
    if 0 > rocket.sprite.y > boss.sprite.y:
        rocket_distance_text.draw()
    if boss.sprite.y < 0:
        boss_distance_text.draw()
    score_text.draw()
    if menu or death:
        menu_texture.draw()
        continue_text.draw()
        esc_text.draw()
        if death:
            loss_text.draw()
        else:
            pause_text.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    print("attempt: " + str(x) + " " + str(y))
    global x_movement, y_movement, shift, space, death, menu
    if menu or death:
        if window.width / 2 - 250 < x < window.width / 2 + 250:
            if window.height / 2 - 250 < y < window.height / 2 + 250:
                print("click")
                if y > window.height / 2:
                    x_movement = 0
                    y_movement = 0
                    shift = False
                    space = False
                    death = False
                    menu = False
                    restart()
            else:
                pass


def insert_enemy():
    car = randint(0, 3)
    if car == 0:
        enemies.append(Enemy(Resources.enemy1_anim, randint(1, 832) + 544, 1920, 0.9, 0, 1))
    if car == 1:
        enemies.append(Enemy(Resources.enemy2_anim, randint(1, 832) + 544, 1920, 0.9, 0, 1))
    if car == 2:
        enemies.append(Enemy(Resources.enemy3_anim, randint(1, 832) + 544, 1920, 0.9, 0, 1))
    if car == 3:
        enemies.append(Enemy(Resources.enemy4_anim, randint(1, 832) + 544, 1920, 0, 0, 1))


def update(dt):
    global enemy_counter, space, death, menu
    if player.health <= 0:
        death = True
    if death or menu:
        return
    else:
        enemy_counter += 1
        if 1 == enemy_counter:
            insert_enemy()
        enemy_counter %= 30
        map_move = player.update(x_movement, y_movement + space * 1.5)
        game_map.update(map_move)
        enemies.update(map_move, particles)
        boss.update(map_move, player.sprite.x, player.sprite.y)
        rocket.update(map_move, player.sprite.x, player.sprite.y, boss.sprite.x, boss.sprite.y)
        enemies.update_collision(player)
        enemies.update_boss_collision(boss)
        player.health += heart.update(player.sprite.x, player.sprite.y, player.width, player.length, map_move)
        health_bar.update(player.health)
        stamina_bar.update(player.stamina)
        particles.update(map_move)
        if rocket.collision_update(player.sprite.x, player.sprite.y, player.width, player.length):
            player.health -= 25
            particles.append(Particle(Resources.explosion_anim, rocket.sprite.x,
                                      rocket.sprite.y, 0.2, 0,
                                      0, 30))
            rocket.sprite.y = boss.sprite.y - 6000
        if boss.collision_update(player.sprite.x, player.sprite.y, player.width, player.length):
            death = True
        boss_distance_text.x = boss.sprite.x
        boss_distance_text.text = str(int(-boss.sprite.y / 100)) + " m"
        rocket_distance_text.x = rocket.sprite.x
        rocket_distance_text.text = str(int(-rocket.sprite.y / 100)) + " m"
        score_text.text = "SCORE:" + str(int(player.score))


def restart():
    global player, game_map, particles, enemies, heart, boss
    player = Player(Resources.player_anim, 720, 10)
    game_map = Map(Resources.texture, Resources.texture, Resources.road)
    particles = Particles()
    enemies = Enemies()
    heart = Health(Resources.heart, 50)
    boss = Boss(Resources.tank_anim, -1000, -1000)


if __name__ == '__main__':
    player = Player(Resources.player_anim, 720, 10)
    game_map = Map(Resources.texture, Resources.texture, Resources.road)
    particles = Particles()
    enemies = Enemies()
    heart = Health(Resources.heart, 50)
    boss = Boss(Resources.tank_anim, -1000, -1000)
    rocket = Rocket(Resources.rocket_anim, -1000, -1000)
    health_bar = Bar(Resources.health_bar, Resources.health_bar_bit, 10, 10, 125)
    stamina_bar = Bar(Resources.stamina_bar, Resources.stamina_bar_bit, 10, 50, 1000)

    boss_distance_text = pyglet.text.Label(x=700, y=10)
    boss_distance_text.italic = True
    boss_distance_text.bold = True
    boss_distance_text.font_size = 16
    boss_distance_text.color = (255, 255, 255, 175)

    rocket_distance_text = pyglet.text.Label(x=700, y=30)
    rocket_distance_text.italic = True
    rocket_distance_text.bold = True
    rocket_distance_text.font_size = 16
    rocket_distance_text.color = (255, 0, 0, 255)

    score_text = pyglet.text.Label(x=10, y=window.height - 60)
    score_text.italic = True
    score_text.bold = True
    score_text.font_size = 32
    score_text.color = (200, 200, 200, 175)

    loss_text = pyglet.text.Label(text="Looks like you are dead", x=window.width / 2 - 250, y=window.height / 2 + 200)
    loss_text.italic = True
    loss_text.bold = True
    loss_text.font_size = 28
    loss_text.color = (230, 30, 30, 175)

    pause_text = pyglet.text.Label(text="Paused", x=window.width / 2 - 105, y=window.height / 2 + 200)
    pause_text.italic = True
    pause_text.bold = True
    pause_text.font_size = 36
    pause_text.color = (30, 230, 30, 175)

    continue_text = pyglet.text.Label(text="Press P to continue", x=window.width / 2 - 240,
                                      y=window.height / 2)
    continue_text.italic = True
    continue_text.bold = True
    continue_text.font_size = 32
    continue_text.color = (30, 30, 30, 175)

    esc_text = pyglet.text.Label(text="Press esc to exit", x=window.width / 2 - 210, y=window.height / 2 - 200)
    esc_text.italic = True
    esc_text.bold = True
    esc_text.font_size = 32
    esc_text.color = (30, 30, 30, 175)

    menu_texture = pyglet.sprite.Sprite(Resources.menu, x=window.width / 2 - 250, y=window.height / 2 - 250)

    pyglet.clock.schedule_interval(update, 1.0 / 60)
    pyglet.app.run()
