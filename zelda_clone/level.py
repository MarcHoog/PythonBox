import pygame
import logging

from settings import *
from tile import Tile
from player import Player as TestPlayer
from random import choice
from debug import debug
from support import import_csv_layout, import_graphics_from
from weapon import WeaponSprite
from ui import UI
from enemy import Enemy


class Level:
    """
    Represents an level object
    """

    def __init__(self, logger: logging.Logger = None):
        # Get display surface From Global
        self.display_surface = pygame.display.get_surface()

        # Logging
        self._logger = logger or logging.getLogger(__name__)
        self._logger.info("Initializing level Class")

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Initializing Stuff
        self.player = None
        self.create_map()

        # user interface
        self.ui = UI()

        # Combat
        self.current_attack = None

    # noinspection PyTypeChecker
    def create_map(self):
        """
        Creates the map for the level
        """

        self._logger.info('Initializing layouts into dictionary:')
        layouts = {
            'invisible_boundary': import_csv_layout('./assets/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('./assets/map/map_Grass.csv'),
            'object': import_csv_layout('./assets/map/map_Objects.csv'),
            'entities': import_csv_layout('./assets/map/map_Entities.csv'),
        }
        self._logger.info(f'\t {layouts}')

        self._logger.info('Initializing graphics into dictionary:')
        graphics = {
            'grass': import_graphics_from('./assets/graphics/grass'),
            'object': import_graphics_from('./assets/graphics/objects')
        }
        self._logger.info(f'\t {graphics}')

        for style, layout in layouts.items():
            self._logger.info(f'Initializing The {style} layout from:')
            for row_index, row in enumerate(layout):
                self._logger.info(f'\t {row}')
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'invisible_boundary':
                            Tile((x, y), [self.obstacle_sprites], style)
                        elif style == 'grass':
                            random_grass_image = choice(graphics[style])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], style,
                                 surface=random_grass_image)
                        elif style == 'object':
                            # TODO MAKE OBJECTS MORE COMPLEX I WANNE BE ABLE TO CUT A TREE DAMMIT!
                            surface = graphics['object'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], style,
                                 surface)
                        elif style == 'entities':
                            if col == '394':
                                self.player = TestPlayer((x, y), [self.visible_sprites], self.obstacle_sprites,
                                                         self.create_attack, self.destroy_attack,
                                                         self.create_magic, self.destroy_magic)
                            else:
                                if col == '390':
                                    monster_name = 'bamboo'
                                elif col == '391':
                                    monster_name = 'spirit'
                                elif col == '392':
                                    monster_name = 'raccoon'
                                else:
                                    monster_name = 'squid'
                                Enemy(monster_name, (x, y), [self.visible_sprites], self.obstacle_sprites)

    def create_attack(self) -> None:
        # TODO Instead of spawning an instance of the weapon, create a draw function for all weapons
        """
        Weapon must excists within level class so it can interact with all the other sprites in the level class
        The level class is actally were all the sprites live
        :return:
        """
        # TODO add error handeling
        self.current_attack = WeaponSprite(self.player, [self.visible_sprites])

    def destroy_attack(self) -> None:
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_magic(self, style, strength, cost):
        print(style, strength, cost)

    def destroy_magic(self):
        pass

    def run(self):
        """
        Runs the Level
        :return:
        """
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.enemy_update(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)
        # DEBUG FUNCTION
        # debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    """
    This sprite group will function as a camera
    Using the Vector 2 to offset the rect and thus blit the image
    somewhere else on the screen.

    For sprite in sprites():
        surface.blit(sprites.image,sprite.rect + Offset (Comes from player)
    """

    # general setup
    def __init__(self, logger: logging.Logger = None):
        # LOGGING
        self._logger = logger or logging.getLogger(__name__)
        self._logger.info("Initializing Custom Camera class")

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        # LOGGING
        self._logger.info(f'Half Width: {self.half_width}')
        self._logger.info(f'Half Height: {self.half_height}')

        self.offset = pygame.math.Vector2()

        # Creating the floor
        self.floor_surface = pygame.image.load('./assets/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # Creating the offset using the player's position
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        """
        Drawing the sprite
        TODO: learn more about lamda
        Sorts the sprites based on there y value, Because of this we overlap all the sprites above us
        REASON: (Because you overlap sprites that are drawn before you)
        And the sprites below us overlap the player, This together with the, Changed hitbox
        Creates the illusion of depth
        In game engine like Godot this is called y sorted
        """
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            """
            Debug message to better understand the camera
            DEMO START
            debug_message = f"SPRITE RECT TOPLEFT: {sprite.rect.topleft} -- " \
                           f"SELF.OFFSET: {self.offset} -- " \
                           f"OFFSET_POSITION: {offset_position}"
            debug(debug_message)
            DEMO END
            """
            self.display_surface.blit(sprite.image, offset_position)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if isinstance(sprite, Enemy)]
        for sprite in enemy_sprites:
            sprite.enemy_update(player)
