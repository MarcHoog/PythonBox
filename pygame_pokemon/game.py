from game_state import GameState
import pygame
import sys
import color_library as cl  
from settings import *

from tile import Tile
from player import Player

class Game(GameState):

    def __init__(self,display) -> None:
        super().__init__(display)
        
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
        self._create_map() 

    def update(self):
        self.visible_sprites.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             
    def _create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x,y),self.visible_sprites)


    def draw(self):
        self.display.fill(cl.PURPLE)
        self.visible_sprites.draw(self.display)