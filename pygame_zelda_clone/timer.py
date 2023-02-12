import pygame


class CooldownTimer:
    """Timer class for cooldowns, so I don't need to relay on cool down definition"""

    def __init__(self, cooldown):
        self.start_time = None
        self.cooldown = cooldown
        self.is_active = False

    @property
    def is_done(self):
        if self.is_active:
            # if timer is active calculate if it is done
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.cooldown:
                self.is_active = False
                return True
            else:
                return False
        # returns old value
        return True

    def _start(self):
        self.start_time = pygame.time.get_ticks()
        self.is_active = True

    def start(self):
        self._start()
