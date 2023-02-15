import logging
import pygame

from debug import debug
from statemachine import StateMachine, Idle, Movement, Attack, Magic
from settings import WEAPON_DATA, MAGIC_DATA
from entity import Entity
from timer import CooldownTimer
from equipment import Equipment


class Player(Entity):

    def __init__(self, position, groups, obstacle_sprites,
                 create_attack, destroy_attack,
                 create_magic, destroy_magic,
                 logger: logging.Logger = None):
        super().__init__(groups)

        # Logging
        self._logger = logger or logging.getLogger(__name__)

        # Image placing
        self.image = pygame.image.load("assets/graphics/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

        # Movement/Direction Stuff
        self.facing = 'down'
        self.obstacle_sprites = obstacle_sprites

        # Collision
        self.hitbox = self.rect.inflate(0, -26)

        # ---------------------------------------
        # ATTACKING
        # ---------------------------------------

        self.create_attack = create_attack
        self.destroy_attack = destroy_attack

        # weapon switching
        self.weapon_timer = CooldownTimer(200)
        self.weapon = Equipment(WEAPON_DATA)

        # ---------------------------------------
        # MAGIC
        # ---------------------------------------

        self.create_magic = create_magic
        self.destroy_magic = destroy_magic

        # magic switching
        self.magic_timer = CooldownTimer(200)
        self.magic = Equipment(MAGIC_DATA)

        # state stuff
        self.states = {
            'idle': Idle(self),
            'movement': Movement(self),
            'attack': Attack(self),
            'magic': Magic(self)
        }
        self.state_machine = StateMachine(self.states, default_state='idle', logger=self._logger)

        # Stats
        self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'magic': 10, 'speed': 10}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 123
        self.speed = self.stats['speed']

    def global_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self._weapon_switching()
        elif keys[pygame.K_e]:
            self._magic_switching()

    def _weapon_switching(self):
        if self.weapon_timer.is_done:
            self.weapon_timer.start()
            self.weapon.next()

    def _magic_switching(self):
        if self.magic_timer.is_done:
            self.magic_timer.start()
            self.magic.next()

    def update(self):
        self.global_input()
        self.state_machine.run()
        self.movement(self.speed)
        debug(f'Current State:{self.state_machine.current_state}, Queue:{self.state_machine.state_queue}')
