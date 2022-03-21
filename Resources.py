import pyglet

starting_texture = pyglet.image.load('Game/assets/sprites/start.png')
road = pyglet.image.load('Game/assets/sprites/road.png')
texture = pyglet.image.load('Game/assets/sprites/texture.png')
enemy1 = pyglet.image.load('Game/assets/sprites/car1.png')
enemy2 = pyglet.image.load('Game/assets/sprites/car2.png')
enemy3 = pyglet.image.load('Game/assets/sprites/car4.png')
enemy4 = pyglet.image.load('Game/assets/sprites/car5.png')
player = pyglet.image.load('Game/assets/sprites/car3.png')
heart = pyglet.image.load('Game/assets/sprites/heart.png')
menu = pyglet.image.load('Game/assets/sprites/menu.png')
rocket = pyglet.image.load('Game/assets/sprites/rocket.png')
tank = pyglet.image.load('Game/assets/sprites/tank.png')
fire_car = pyglet.image.load('Game/assets/sprites/explosion.png')
explosion = pyglet.image.load('Game/assets/sprites/explosion_round.png')
health_bar_bit = pyglet.image.load('Game/assets/sprites/health_bar_bit.png')
stamina_bar = pyglet.image.load('Game/assets/sprites/stamina_bar.png')
health_bar = pyglet.image.load('Game/assets/sprites/health_bar.png')
stamina_bar_bit = pyglet.image.load('Game/assets/sprites/stamina_bar_bit.png')

enemy1_seq = pyglet.image.ImageGrid(enemy1, 1, 2, item_width=128, item_height=192)
enemy1_texture = pyglet.image.TextureGrid(enemy1_seq)
enemy1_anim = pyglet.image.Animation.from_image_sequence(enemy1_texture[0:], 0.5, loop=True)

enemy2_seq = pyglet.image.ImageGrid(enemy2, 1, 2, item_width=128, item_height=192)
enemy2_texture = pyglet.image.TextureGrid(enemy2_seq)
enemy2_anim = pyglet.image.Animation.from_image_sequence(enemy2_texture[0:], 0.5, loop=True)

enemy3_seq = pyglet.image.ImageGrid(enemy3, 1, 2, item_width=128, item_height=192)
enemy3_texture = pyglet.image.TextureGrid(enemy3_seq)
enemy3_anim = pyglet.image.Animation.from_image_sequence(enemy3_texture[0:], 0.5, loop=True)

enemy4_seq = pyglet.image.ImageGrid(enemy4, 1, 2, item_width=128, item_height=192)
enemy4_texture = pyglet.image.TextureGrid(enemy4_seq)
enemy4_anim = pyglet.image.Animation.from_image_sequence(enemy4_texture[0:], 1, loop=True)

player_seq = pyglet.image.ImageGrid(player, 1, 2, item_width=128, item_height=192)
player_texture = pyglet.image.TextureGrid(player_seq)
player_anim = pyglet.image.Animation.from_image_sequence(player_texture[0:], 0.5, loop=True)
tank_seq = pyglet.image.ImageGrid(tank, 1, 2, item_width=162, item_height=243)
tank_texture = pyglet.image.TextureGrid(tank_seq)
tank_anim = pyglet.image.Animation.from_image_sequence(tank_texture[0:], 0.05, loop=True)

fire_car_seq = pyglet.image.ImageGrid(fire_car, 1, 8, item_width=128, item_height=192)
fire_car_texture = pyglet.image.TextureGrid(fire_car_seq)
fire_car_anim = pyglet.image.Animation.from_image_sequence(fire_car_texture[0:], 0.2, loop=True)

explosion_seq = pyglet.image.ImageGrid(explosion, 1, 12, item_width=192, item_height=192)
explosion_texture = pyglet.image.TextureGrid(explosion_seq)
explosion_anim = pyglet.image.Animation.from_image_sequence(explosion_texture[0:], 0.1, loop=True)

rocket_seq = pyglet.image.ImageGrid(rocket, 1, 2, item_width=32, item_height=150)
rocket_texture = pyglet.image.TextureGrid(rocket_seq)
rocket_anim = pyglet.image.Animation.from_image_sequence(rocket_texture[0:], 0.2, loop=True)

# explosion = pyglet.media.load('res/sounds/exp_01.wav', streaming=False)
