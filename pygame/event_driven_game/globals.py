from random import randrange
EVENT_TYPES = [
    "PLAYER_HIT_EVENT",  
    "PLAYER_DEATH_EVENT", 
    "PLAYER_MOVE_EVENT",
    "PRINT",
    "INPUT",
    "MOVEMENT",
    "QUIT",
    ]


WIDTH = 800
HEIGHT = 800
TILE_SIZE = 32
RANGE = (0,WIDTH,TILE_SIZE)

get_random_position = lambda: (randrange(*RANGE), randrange(*RANGE))