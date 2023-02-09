GAME_NAME = "Kings and Nature"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60
TILESIZE = 64

# ui
BAR_HEIGHT = 40
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = './assets/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# COLORS
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#493736'
UI_HIGHLIGHT_COLOR = '#ffc27f'
TEXT_COLOR = '#EEEEEE'

# UI COLOR
HEALTH_COLOR = '#c84648'
ENERGY_COLOR = '#7cb490'
UI_BORDER_COLOR_ACTIVE = 'gold'

WEAPON_DATA = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': './assets/graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': './assets/graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 400, 'damage': 30, 'graphic': './assets/graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 10, 'graphic': './assets/graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': './assets/graphics/weapons/sai/full.png'}}

MAGIC_DATA = {
    'flame': {'strength': 5, 'cost': 15, 'graphic': './assets/graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': './assets/graphics/particles/heal/heal.png'}}

MONSTER_DATA = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash',
              'attack_sound': './assets/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80,
              'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw',
                'attack_sound': './assets/audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120,
                'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder',
               'attack_sound': './assets/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60,
               'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack',
               'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50,
               'notice_radius': 300}}
