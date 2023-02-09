from abc import ABC, abstractmethod
import pygame
import logging
from timer import CooldownTimer
from support import import_player_animations
from settings import MAGIC_DATA


class StateMachine:

    def __init__(self, states, default_state, logger: logging.Logger = None):

        self._logger = logger or logging.getLogger(__name__)
        self._logger.info('Initializing State Machine')
        self.default_state = default_state
        self.states = states
        self.state_queue = []

        # Setting up for the first state
        self.state_queue.append(self.states[self.default_state])
        self.current_state = self.state_queue[-1]
        self.current_state.enter()

    def push_state(self, new_state):
        self.state_queue.append(self.states[new_state])

    def run(self):
        previous_state = self.current_state

        if self.current_state.status == 'done':
            self.state_queue.pop()
            if self.current_state.next != 'previous':
                self.push_state(self.current_state.next)
        elif self.current_state.status == 'interrupted':
            self.push_state(self.current_state.next)

        self.current_state = self.state_queue[-1]

        if self.current_state != previous_state:
            previous_state.exit()
            previous_state.status = 'inactive'
            self.current_state.status = 'active'
            self.current_state.enter()

        self.current_state.update()


class State(ABC):

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def update(self):
        pass


class BaseState(State):
    def __init__(self, player, animation_template, animation_name: str = ''):
        self.player = player
        self.animation_template = animation_template
        self.animations = import_player_animations(self.animation_template)
        self.animation_name = animation_name

    def animate(self):
        animation = self.animations[f'{self.player.facing}{self.animation_name}']

        # loop over each animation
        self.player.frame_index += self.player.animation_speed
        if self.player.frame_index >= len(animation):
            self.player.frame_index = 0

        # set the image
        self.player.image = animation[int(self.player.frame_index)]
        self.player.rect = self.player.image.get_rect(center=self.player.hitbox.center)

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Idle(BaseState):
    animation_template = {'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': []}
    animation_name = '_idle'

    def __init__(self, player):
        super().__init__(player, self.animation_template, self.animation_name)
        self.status = 'inactive'
        self.player = player
        self.next = None

    def enter(self):
        pass

    def exit(self):
        pass

    def input(self):
        keys = pygame.key.get_pressed()
        movement_keys = [keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT]]
        combat_keys = [keys[pygame.K_LCTRL]]
        magic_keys = [keys[pygame.K_SPACE]]
        for key in movement_keys:
            if key:
                self.status = 'interrupted'
                self.next = 'movement'
        for key in combat_keys:
            if key:
                self.status = 'interrupted'
                self.next = 'attack'
        for key in magic_keys:
            if key:
                self.status = 'interrupted'
                self.next = 'magic'

    def update(self):
        self.animate()
        self.input()


class Movement(BaseState):
    animation_template = {'right': [], 'left': [], 'up': [], 'down': []}
    animation_name = ''

    def __init__(self, player):
        super().__init__(player, self.animation_template, self.animation_name)

        self.player = player
        self.status = 'inactive'
        self.next = None

    def enter(self):
        pass

    def exit(self):
        pass

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.direction.y = -1
            self.player.facing = 'up'

        elif keys[pygame.K_DOWN]:
            self.player.direction.y = 1
            self.player.facing = 'down'
        else:
            # Resets moving so we don't keep walking
            self.player.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.player.direction.x = -1
            self.player.facing = 'left'

        elif keys[pygame.K_RIGHT]:
            self.player.direction.x = 1
            self.player.facing = 'right'
        else:
            # Resets moving so we don't keep walking
            self.player.direction.x = 0

        # attack input
        if keys[pygame.K_SPACE]:
            self.status = 'interrupted'
            self.next = 'magic'

        # magic input
        if keys[pygame.K_LCTRL]:
            self.status = 'interrupted'
            self.next = 'attack'

        if self.player.direction == (0, 0):
            self.status = 'done'
            self.next = 'previous'

    def update(self):
        self.animate()
        self.input()


class Action(BaseState):
    animation_template = {'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}
    animation_name = '_attack'

    def __init__(self, player):
        super().__init__(player, self.animation_template, self.animation_name)

        self.status = 'inactive'
        self.next = 'previous'

        self.player = player
        self.action = CooldownTimer(400)

    def update(self):
        self.animate()
        if self.action.is_done:
            self.status = 'done'
            self.next = 'previous'


class Attack(Action):

    def __init__(self, player):
        super().__init__(player)

    def enter(self):
        self.action.start()
        self.player.create_attack()
        self.player.direction.x = 0
        self.player.direction.y = 0

    def exit(self):
        self.player.destroy_attack()


class Magic(Action):
    def __init__(self, player):
        super().__init__(player)

    def enter(self):
        self.action.start()

        spell = self.player.magic_style
        spell_values = list(MAGIC_DATA.values())[self.player.magic_index]
        strength = spell_values['strength'] + self.player.stats['magic']
        cost = spell_values['cost']

        self.player.create_magic(spell, strength, cost)
        self.player.direction.x = 0
        self.player.direction.y = 0

    def exit(self):
        self.player.destroy_magic()


# Monster states

if __name__ == "__main__":
    pass
