import pygame

from entity import Entity
from statemachine import StateMachine
from support import import_graphics_from
from settings import MONSTER_DATA
from collections import namedtuple


class Enemy(Entity):
    """Enemy class for the game. Inherits from Entity class."""
    def __init__(self, monster_name, pos, groups, obstacle_sprites):
        # general
        super().__init__(groups)

        # stats
        self.sprite_type = 'enemy'
        self.monster_name = monster_name
        monster_info = MONSTER_DATA[monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        self.animations = {}

        # graphics setup
        self.import_graphics(monster_name)
        self.state = 'idle'
        print(self.animations)
        self.image = self.animations[self.state][self.frame_index].convert_alpha()

        # movement
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown_time = 400

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        main_path = f'./assets/graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_graphics_from(main_path + animation)

    def get_player_distance_direction(self, player):
        player_dist_rect = namedtuple('PlayerDistanceDirection', ['distance', 'direction'])

        enemy_vect = pygame.math.Vector2(self.rect.center)
        player_vect = pygame.math.Vector2(player.rect.center)
        distance = (player_vect - enemy_vect).magnitude()

        if distance > 0:
            direction = (player_vect - enemy_vect).normalize()
        else:
            direction = pygame.math.Vector2(0, 0)

        return player_dist_rect(distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player).distance

        if distance <= self.attack_radius and self.can_attack:
            if self.state != 'attack':
                self.frame_index = 0
            self.state = 'attack'

        elif distance <= self.notice_radius:
            self.state = 'move'
        else:
            self.state = 'idle'

    def attack_cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()

            if current_time - self.attack_time >= self.attack_cooldown_time:
                self.can_attack = True

    def actions(self, player):
        if self.state == 'attack':
            self.attack_time = pygame.time.get_ticks()
        elif self.state == 'move':
            self.direction = self.get_player_distance_direction(player).direction
        else:
            self.direction = pygame.math.Vector2(0, 0)

    def animate(self):
        animation = self.animations[self.state]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations[self.state]):
            if self.state == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)].convert_alpha()
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.movement(self.speed)
        self.animate()
        self.attack_cooldown()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)
