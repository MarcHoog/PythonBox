import pygame
import sys
import color_library as cl  

from abc import ABC, abstractmethod
from tile import Tile
from player import Player
from settings import *

class GameState(ABC):

    def __init__(self,display):
        self.display = display
        self.transition = None

    def set_transition(self, transition):
        self.transition = transition

    def enter(self):
        pass
    
    def exit(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass

class GameStateManager:
    def __init__(self):
        self.states = {'main_menu': MainMenu,
                       'game': Game,}

        self.state = None
        self.default = 'game'
        
        self.display = pygame.display.get_surface()
        self.player = 'player'
        
        self.change_state(self.default)


    def change_state(self, new_state):
        if self.state:
            self.state.exit()
        self.state = self.states[new_state](self.display)
        self.state.enter()

    def run(self):
        if self.state.transition and self.state.transition != self.state:
            self.change_state(self.state.transition)
        self.state.update()
        self.state.draw()
        
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
        
class MainMenu(GameState):

    def __init__(self,display) -> None:
        super().__init__(display)


    def update(self):
        pass

    def draw():
        pass