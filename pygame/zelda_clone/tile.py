import pygame
from pygame.sprite import AbstractGroup

from settings import *


class Tile(pygame.sprite.Sprite):
    """
    A tile in the game world.
    """

    def __init__(self, position, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            # do an offset
            self.rect = self.image.get_rect(topleft=(position[0], position[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=position)

        # Makes the hitbox of the sprite slightly smaller
        # We use hitbox in the player collision code in oldplayer.py
        # We do this so there is a small overlap in the sprites
        # Meaning you can stand infront of behind somebody or something
        self.hitbox = self.rect.inflate(0, -10)
